const wppconnect = require('@wppconnect-team/wppconnect');
const { spawn } = require('child_process');

const processosAtivos = {}; // Armazena sessões ativas de usuários com o Python

wppconnect.create({
    session: 'bot_juridico',
    headless: true,
    useChrome: true,
})
.then(client => {
    console.log('✅ Bot do WhatsApp está rodando!');

    client.onMessage(async message => {
        const chatId = message.from;
        const texto = message.body.trim();

        if (texto.toLowerCase() === "!jus") {
            await client.sendText(chatId, "⏳ Iniciando consulta jurídica... Aguarde.");

            // Iniciar um processo Python para cada usuário
            const pythonProcess = spawn('python', ['src/main.py'], {
                stdio: ['pipe', 'pipe', 'pipe'],
                env: { ...process.env, PYTHONUTF8: '1' } // Garante que o Python use UTF-8
            });

            processosAtivos[chatId] = pythonProcess;

            pythonProcess.stdout.on('data', async (data) => {
                const resposta = data.toString().trim();
                console.log(`📜 Resposta do Python para ${chatId}: ${resposta}`);
                await client.sendText(chatId, resposta);
            });

            pythonProcess.stderr.on('data', (data) => {
                console.error(`❌ Erro no Python para ${chatId}: ${data.toString()}`);
            });

            pythonProcess.on('close', () => {
                console.log(`📌 Processo Python finalizado para ${chatId}`);
                delete processosAtivos[chatId]; // Remover sessão quando terminar
            });

        } else if (processosAtivos[chatId]) {
            // Se já existe um processo Python ativo, passar a resposta do usuário para ele
            const pythonProcess = processosAtivos[chatId];
            pythonProcess.stdin.write(texto + '\n');
        }
    });
})
.catch(error => console.log('Erro ao iniciar o bot:', error));
