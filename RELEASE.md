# Release v1.0.0

## 🎉 Novidades
- Primeira versão pública do TheLawyer
- Sistema de consulta jurídica via WhatsApp
- Integração com DataJud para consulta de processos
- Processamento e interpretação de documentos PDF
- Uso da API OpenAI para análise jurídica

## 🔧 Melhorias
- Proteção de informações sensíveis
  - Chaves de API movidas para variáveis de ambiente
  - Números de telefone protegidos
  - Arquivos sensíveis adicionados ao .gitignore
- Documentação completa
  - README.md atualizado com instruções detalhadas
  - Templates de configuração (.env.example e permitidos.csv.example)
  - Seção de segurança adicionada

## 🐛 Correções
- Remoção de informações sensíveis do histórico do Git
- Organização do código e estrutura do projeto
- Melhorias na segurança e privacidade

## 📦 Arquivos Incluídos
- `index.js` - Script principal do bot
- `src/` - Código fonte Python
  - `config.py` - Configurações do sistema
  - `main.py` - Lógica principal
  - `pdf_processor.py` - Processamento de PDFs
  - `openai_interpreter.py` - Integração com OpenAI
- `requirements.txt` - Dependências Python
- `package.json` - Dependências Node.js
- `.env.example` - Template de variáveis de ambiente
- `permitidos.csv.example` - Template de números permitidos

## ⚠️ Notas Importantes
- É necessário configurar as chaves de API no arquivo `.env`
- Os números de telefone permitidos devem ser configurados no arquivo `permitidos.csv`
- O bot requer uma conexão com a internet para funcionar
- É necessário ter uma conta no DataJud para consultas processuais

## 🔄 Próximos Passos
- Implementação de mais funcionalidades jurídicas
- Melhorias na interface do usuário
- Suporte a mais formatos de documento
- Otimização do processamento de PDFs

## 📝 Créditos
Desenvolvido por Pablo Murad - 2025 