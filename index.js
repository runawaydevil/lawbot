const wppconnect = require('@wppconnect-team/wppconnect');
const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');
const csv = require('csv-parser');

const processosAtivos = {};
const estadosUsuarios = {};
let numerosPermitidos = new Set();

const uploadDir = path.join(__dirname, 'uploads');
if (!fs.existsSync(uploadDir)) {
    fs.mkdirSync(uploadDir);
}

function carregarNumerosPermitidos() {
    if (fs.existsSync('permitidos.csv')) {
        fs.createReadStream('permitidos.csv')
            .pipe(csv({ headers: false }))
            .on('data', (row) => {
                const numero = Object.values(row)[0].trim();
                numerosPermitidos.add(`${numero}@c.us`);
            })
            .on('end', () => {
                console.log('✅ Números permitidos carregados:', [...numerosPermitidos]);
            });
    } else {
        console.log('⚠️ Arquivo permitidos.csv não encontrado. Todos os números serão bloqueados.');
    }
}
carregarNumerosPermitidos();

wppconnect.create({ session: 'bot_juridico', headless: true, useChrome: true })
.then(client => {
    console.log('✅ Bot do WhatsApp está rodando!');

    client.onMessage(async message => {
        const chatId = message.from;
        const texto = message.body ? message.body.trim() : "";
        const isPDF = message.mimetype === 'application/pdf';
        const isDOCX = message.mimetype === 'application/vnd.openxmlformats-officedocument.wordprocessingml.document';

        if (!numerosPermitidos.has(chatId)) return;

        if (texto.toLowerCase() === "!dev") {
            await client.sendText(chatId, "👨‍💻 Criado e mantido por Pablo Murad - 2025");
            return;
        }

        if (!estadosUsuarios[chatId]) {
            await client.sendText(chatId, "👋 Como posso lhe ajudar? Escolha uma opção:\n1️⃣ Pesquisar Processo\n2️⃣ Interpretar Documentos");
            estadosUsuarios[chatId] = "menu_principal";
            return;
        }

        switch(estadosUsuarios[chatId]) {
            case "menu_principal":
                if (texto === "1") {
                    await client.sendText(chatId, "✏️ Digite o número do processo:");
                    estadosUsuarios[chatId] = "aguardando_numero_processo";
                } else if (texto === "2") {
                    await client.sendText(chatId, "📎 Envie o documento em PDF ou DOCX para interpretação.");
                    estadosUsuarios[chatId] = "aguardando_documento";
                }
                break;

            case "aguardando_numero_processo":
                processosAtivos[chatId] = { numeroProcesso: texto };
                await client.sendText(chatId, "✏️ Digite o código do tribunal:");
                estadosUsuarios[chatId] = "aguardando_tribunal";
                break;

            case "aguardando_tribunal":
                processosAtivos[chatId].tribunal = texto.toUpperCase();
                await client.sendText(chatId, "⏳ Processando consulta, aguarde...");

                const pythonProcess = spawn('python', ['src/main.py'], {
                    stdio: ['pipe', 'pipe', 'pipe'],
                    env: { ...process.env, PYTHONUTF8: '1' }
                });

                pythonProcess.stdin.write(`${processosAtivos[chatId].numeroProcesso}\n`);
                pythonProcess.stdin.write(`${processosAtivos[chatId].tribunal}\n`);
                pythonProcess.stdin.end();

                let bufferResposta = "";

                pythonProcess.stdout.on('data', (data) => {
                    bufferResposta += data.toString();
                });

                pythonProcess.on('close', async () => {
                    const inicioIA = bufferResposta.indexOf('*Detalhes do Processo:*');
                    const respostaFinal = inicioIA !== -1 ? bufferResposta.slice(inicioIA).trim() : null;
                    if (respostaFinal) {
                        await client.sendText(chatId, respostaFinal);
                    } else {
                        await client.sendText(chatId, "⚠️ Não foi possível obter informações do processo.");
                    }
                    delete estadosUsuarios[chatId];
                    delete processosAtivos[chatId];
                });
                break;

            case "aguardando_documento":
                if (isPDF || isDOCX) {
                    const ext = isPDF ? 'pdf' : 'docx';
                    await client.sendText(chatId, "⏳ Interpretando...");
                    const buffer = await client.decryptFile(message);
                    const filePath = path.join(uploadDir, `${chatId}.${ext}`);
                    fs.writeFileSync(filePath, buffer);

                    const docProcess = spawn('python', ['src/pdf_processor.py', filePath]);
                    let docResultado = "";

                    docProcess.stdout.on('data', data => {
                        docResultado += data.toString();
                    });

                    docProcess.on('close', async () => {
                        await client.sendText(chatId, docResultado.trim() || "⚠️ Erro na interpretação.");
                        delete estadosUsuarios[chatId];
                    });
                } else {
                    await client.sendText(chatId, "⚠️ Envie um documento PDF ou DOCX válido.");
                }
                break;

            default:
                delete estadosUsuarios[chatId];
                break;
        }
    });
})
.catch(error => console.log('Erro ao iniciar o bot:', error));