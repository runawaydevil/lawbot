# 🤖 TheLawyer - Consulta Jurídica via WhatsApp

**Desenvolvido por Pablo Murad**

## 📋 Sobre o Projeto
TheLawyer é um sistema de automação para consultas jurídicas que permite a pesquisa de processos via DataJud diretamente pelo WhatsApp, além de interpretar documentos jurídicos em PDF.

## ✨ Funcionalidades
- Consulta de processos via DataJud por número de processo ou CPF/CNPJ
- Processamento de arquivos PDF para extração e interpretação de informações jurídicas
- Envio automático das respostas formatadas via WhatsApp
- Uso da API OpenAI para interpretar movimentações processuais e documentos jurídicos

## 🚀 Começando

### Pré-requisitos
- Node.js 18+
- Python 3.x
- Conta no DataJud
- Chave de API da OpenAI

### 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/runawaydevil/lawbot.git
cd lawbot
```

2. Instale as dependências do Node.js:
```bash
npm install
```

3. Instale as dependências do Python:
```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
   - Copie o arquivo `.env.example` para `.env`
   - Edite o arquivo `.env` com suas chaves de API:
     ```
     DATAJUD_API_KEY="sua_chave_api_aqui"
     OPENAI_API_KEY="sua_chave_api_aqui"
     ```

5. Configure os números permitidos:
   - Copie o arquivo `permitidos.csv.example` para `permitidos.csv`
   - Adicione os números de telefone que terão acesso ao sistema (formato: 55DDDXXXXXXXX)

## 📱 Uso

1. Inicie o bot:
```bash
node index.js
```

2. Escaneie o QR Code que aparecerá no terminal usando o WhatsApp no seu celular

3. Comandos disponíveis:
   - `!jus` → Iniciar consulta jurídica
   - `!law` → Enviar um PDF para análise jurídica
   - Enviar um PDF diretamente → O bot analisará o documento e fornecerá um resumo jurídico

## 🛠 Tecnologias Utilizadas
- **Node.js** - Ambiente de execução JavaScript
- **Python** - Linguagem de programação
- **WPPConnect** - Integração com WhatsApp
- **OpenAI API** - Interpretação de movimentações jurídicas
- **PyMuPDF (fitz)** - Extração de texto de PDFs

## 🔒 Segurança
- O arquivo `.env` contém chaves de API sensíveis e não deve ser compartilhado
- O arquivo `permitidos.csv` contém números de telefone autorizados e não deve ser compartilhado
- Ambos os arquivos estão no `.gitignore` para evitar exposição acidental

## 📝 Licença
Este projeto é livre e pode ser usado e modificado sem restrições.

## 🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📞 Suporte
Para suporte, entre em contato através do WhatsApp ou abra uma issue no GitHub.

