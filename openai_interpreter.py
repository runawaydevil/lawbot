import os
from openai import OpenAI
from dotenv import load_dotenv

# Carregar variáveis do ambiente
load_dotenv()

# Criar cliente OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def interpretar_movimentacoes(movimentacoes, numero_processo, tribunal):
    """Gera um relatório sobre o status do processo e sugestões de ações futuras baseadas na legislação brasileira."""

    if not movimentacoes:
        return "Nenhuma movimentação encontrada para análise."

    prompt = f"""
    Você é um especialista jurídico. Analise as movimentações processuais do processo {numero_processo}, do tribunal {tribunal}, e:
    - Resuma os principais eventos processuais.
    - Informe o status atual do processo.
    - Sugira os próximos passos com base na legislação brasileira.

    Movimentações:
    """
    
    for mov in movimentacoes:
        data = mov.get("dataHora", "Data desconhecida")
        descricao = mov.get("nome", "Movimentação desconhecida")
        prompt += f"- {data}: {descricao}\n"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Erro ao acessar OpenAI: {str(e)}"
