# 📜 TheLawyer - Consulta Jurídica via WhatsApp

**Desenvolvido por Pablo Murad**

## 📌 Sobre o Projeto
TheLawyer é um sistema de automação para consultas jurídicas, desenvolvido utilizando **Python** e **Node.js**. Ele permite a pesquisa de processos via DataJud diretamente pelo WhatsApp, além de interpretar documentos jurídicos em **PDF**.

## ⚖️ Funcionalidades
- Consulta de processos via DataJud por número de processo ou CPF/CNPJ.
- Processamento de arquivos **PDF** para extração e interpretação de informações jurídicas.
- Envio automático das respostas formatadas via WhatsApp.
- Uso da API **OpenAI** para interpretar movimentações processuais e documentos jurídicos.

## 🚀 Instalação e Configuração
O projeto utiliza **Python** e **Node.js**. Siga os passos abaixo para configurar corretamente.

### 1️⃣ Clonar o Repositório
```sh
git clone https://gitlab.com/seu-repositorio/TheLawyer.git
cd TheLawyer
```

### 2️⃣ Configuração do Ambiente Python
Crie um ambiente virtual e instale as dependências.
```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

### 3️⃣ Configuração do Ambiente Node.js
Instale as dependências do Node.js:
```sh
npm install
```

### 4️⃣ Configuração das Variáveis de Ambiente
Crie um arquivo **.env** e configure as credenciais da OpenAI e outras variáveis necessárias:
```sh
touch .env
```
Exemplo do conteúdo do **.env**:
```ini
OPENAI_API_KEY=your-api-key
```

### 5️⃣ Conectar ao WhatsApp
Ao iniciar o bot, será gerado um **QR Code** que precisa ser escaneado pelo WhatsApp no celular. Isso é necessário para autenticar a sessão e permitir a troca de mensagens.

> 📌 **Nota:** Nesta versão, a conexão e operação do bot são realizadas **somente via terminal**.

### 6️⃣ Execução do Bot
Para rodar o bot no WhatsApp, execute:
```sh
node index.js
```

### 7️⃣ Testando o Processamento de PDFs
Para testar a interpretação de um PDF:
```sh
python src/pdf_processor.py caminho/do/arquivo.pdf
```

## 🔄 Comandos do WhatsApp
- `!jus` → Iniciar consulta jurídica.
- `!law` → Enviar um **PDF** para análise jurídica.
- Enviar um **PDF** diretamente → O bot analisará o documento e fornecerá um resumo jurídico.

## 🛠 Tecnologias Utilizadas
- **Python 3.x**
- **Node.js 18+**
- **WPPConnect** para integração com WhatsApp
- **OpenAI API** para interpretação de movimentações jurídicas
- **PyMuPDF (fitz)** para extração de texto de PDFs

## 📜 Licença
Este projeto é **livre** e pode ser usado e modificado sem restrições.

