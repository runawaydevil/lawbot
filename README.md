# TheLaw - Sistema de Consulta Jurídica via WhatsApp

## Desenvolvedor
Este projeto foi desenvolvido por **Pablo Murad**.

## Descrição
O **TheLaw** é um sistema de consulta jurídica automatizado que permite aos usuários **consultar processos jurídicos diretamente no WhatsApp**. O bot interage com os usuários, solicitando informações como o **número do processo**, **CPF/CNPJ** e o **tribunal**, e retorna os detalhes dos processos diretamente do **Datajud**.

### Funcionalidades
- **Consulta por número de processo**: O bot permite que o usuário consulte um processo fornecendo o número do processo e o tribunal.
- **Consulta por CPF/CNPJ**: O usuário pode consultar todos os processos relacionados a um **CPF ou CNPJ**. O bot solicita o número do **tribunal** para realizar a consulta.
- **Integração com WhatsApp**: A comunicação com o usuário é realizada via **WhatsApp** usando a API do **WPPConnect**. O bot responde automaticamente às mensagens e interage de forma fluída com o usuário.
- **Execução de consulta via Python**: O bot utiliza **Python** para realizar a consulta processual, integrando com a API do **Datajud**. O resultado da consulta é retornado para o usuário no WhatsApp.

## Instalação
1. Clone este repositório:

```bash
git clone https://gitlab.com/seu-usuario/thelaw.git
```

2. Entre no diretório do projeto:

```bash
cd thelaw
```

3. Instale as dependências do Node.js:

```bash
npm install
```

4. Configure as variáveis de ambiente, como os tokens de acesso ao WhatsApp, em um arquivo `.env`.

5. Execute o bot:

```bash
node index.js
```

## Como funciona
1. Quando o usuário envia o comando **`!jus`** no WhatsApp, o bot inicia uma conversa para determinar qual tipo de consulta será realizada (número do processo ou CPF/CNPJ).
2. O bot solicita o **número do processo** ou o **CPF/CNPJ** e o **tribunal** para realizar a consulta.
3. O bot chama um script Python (**`main.py`**) que consulta a base de dados do **Datajud** e retorna os resultados para o usuário.
4. O bot exibe os detalhes do processo, como o número do processo, o tribunal, a classe processual, o órgão julgador e os assuntos relacionados.

