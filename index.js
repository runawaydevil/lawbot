const wppconnect = require('@wppconnect-team/wppconnect');
const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

const processosAtivos = {}; // Armazena sessões ativas de usuários com o Python
const estadosUsuarios = {}; // Armazena o estado atual da conversa de cada usuário

// Certifique-se de que o diretório "uploads" existe
const uploadDir = path.join(__dirname, 'uploads');
if (!fs.existsSync(uploadDir)) {
    fs.mkdirSync(uploadDir);
}

wppconnect.create({
    session: 'bot_juridico',
    headless: true,
    useChrome: true,
})
.then(client => {
    console.log('✅ Bot do WhatsApp está rodando!');

    client.onMessage(async message => {
        const chatId = message.from;
        const texto = message.body ? message.body.trim() : "";
        const isMedia = message.isMedia || message.mimetype === 'application/pdf';

        if (isMedia && message.mimetype === 'application/pdf') {
            await client.sendText(chatId, "📄 Recebi seu PDF. Processando, aguarde...");
            
            const buffer = await client.decryptFile(message);
            const filePath = path.join(uploadDir, `${chatId}.pdf`);
            fs.writeFileSync(filePath, buffer);

            const pythonProcess = spawn('python', ['src/pdf_processor.py', filePath]);
            let bufferResposta = "";

            pythonProcess.stdout.on('data', async (data) => {
                bufferResposta += data.toString().trim() + "\n";
            });

            pythonProcess.on('close', async () => {
                console.log(`📌 Processamento de PDF finalizado para ${chatId}`);
                await client.sendText(chatId, bufferResposta.trim() || "⚠️ Ocorreu um erro ao processar o PDF.");
            });
        } 
        else if (texto.toLowerCase() === "!jus") {
            await client.sendText(chatId, "⏳ Iniciando consulta jurídica... Aguarde.");
            await client.sendText(chatId, "🔎 Deseja pesquisar por (1) Número do Processo ou (2) CPF/CNPJ?");
            estadosUsuarios[chatId] = "aguardando_tipo_consulta";
        } else if (estadosUsuarios[chatId] === "aguardando_tipo_consulta") {
            if (texto === "1") {
                await client.sendText(chatId, "Digite o número do processo:");
                estadosUsuarios[chatId] = "aguardando_numero_processo";
            } else if (texto === "2") {
                await client.sendText(chatId, "Digite o CPF ou CNPJ:");
                estadosUsuarios[chatId] = "aguardando_cpf_cnpj";
            } else {
                await client.sendText(chatId, "Opção inválida. Escolha (1) Número do Processo ou (2) CPF/CNPJ.");
            }
        } else if (estadosUsuarios[chatId] === "aguardando_numero_processo") {
            processosAtivos[chatId] = { numeroProcesso: texto };
            await client.sendText(chatId, "Digite o código do tribunal:");
            estadosUsuarios[chatId] = "aguardando_tribunal";
        } else if (estadosUsuarios[chatId] === "aguardando_tribunal") {
            processosAtivos[chatId].tribunal = texto;
            await client.sendText(chatId, "⏳ Processando consulta, aguarde...");

            const pythonProcess = spawn('python', ['src/main.py'], {
                stdio: ['pipe', 'pipe', 'pipe'],
                env: { ...process.env, PYTHONUTF8: '1' }
            });

            pythonProcess.stdin.write(`${processosAtivos[chatId].numeroProcesso}\n`);
            pythonProcess.stdin.write(`${processosAtivos[chatId].tribunal}\n`);
            pythonProcess.stdin.end();

            let bufferResposta = "";
            let capturandoResposta = false;

            pythonProcess.stdout.on('data', async (data) => {
                const resposta = data.toString().trim();
                console.log(`📜 Resposta do Python para ${chatId}: ${resposta}`);

                if (resposta.includes("🔎 **Detalhes do Processo:**")) {
                    capturandoResposta = true;
                    bufferResposta = "";
                }

                if (capturandoResposta) {
                    bufferResposta += resposta + "\n";
                }
            });

            pythonProcess.on('close', async () => {
                console.log(`📌 Processo Python finalizado para ${chatId}`);
                if (bufferResposta.trim()) {
                    await client.sendText(chatId, bufferResposta.trim());
                } else {
                    await client.sendText(chatId, "⚠️ Ocorreu um erro ao processar a consulta.");
                }
                delete estadosUsuarios[chatId];
                delete processosAtivos[chatId];
            });
        }
    });
})
.catch(error => console.log('Erro ao iniciar o bot:', error));