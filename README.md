# 🤖 TheLawyer - Consulta Jurídica via WhatsApp

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Node.js](https://img.shields.io/badge/Node.js-18+-green.svg)](https://nodejs.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-orange.svg)](https://openai.com/)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-Bot-brightgreen.svg)](https://www.whatsapp.com/)
[![DataJud](https://img.shields.io/badge/DataJud-API-lightgrey.svg)](https://datajud.cnj.jus.br/)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)](https://github.com/runawaydevil/lawbot)
[![Version](https://img.shields.io/badge/Version-1.0.0-blue.svg)](https://github.com/runawaydevil/lawbot/releases)
[![Hacker](https://img.shields.io/badge/Hacker-1337-red.svg)](https://www.hackerrank.com/)
[![Security](https://img.shields.io/badge/Security-Protected-brightgreen.svg)](https://www.owasp.org/)

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

MIT License

Copyright (c) 2025 Pablo Murad

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## 🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📞 Suporte
Para suporte, por favor abra uma issue no GitHub.

