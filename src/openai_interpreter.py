import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Ajuste para garantir que o src/ esteja no caminho do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Carregar variáveis do ambiente
load_dotenv()

# Criar cliente OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def interpretar_movimentacoes(movimentacoes, numero_processo, tribunal):
    """Gera um relatório sobre o status do processo e sugestões de ações futuras baseadas na legislação brasileira."""
    if not movimentacoes:
        return "Nenhuma movimentação encontrada para análise."

    prompt = f"""
    Você é um advogado especializado em direito brasileiro. Analise as movimentações processuais do processo {numero_processo}, do tribunal {tribunal}, e:
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

def interpretar_documento(texto):
    """Analisa um documento jurídico enviado pelo usuário e gera um resumo interpretativo."""
    if not isinstance(texto, str) or not texto.strip():
        return "O documento enviado está vazio ou não pode ser interpretado."
    
    termos_juridicos = ["contrato", "ação judicial", "recurso", "sentença", "jurisprudência", "citação", "acórdão", "processo"]
    if not any(termo in texto.lower() for termo in termos_juridicos):
        return "⚠️ O documento enviado não parece ser de contexto jurídico. Por favor, envie um documento relacionado ao direito."
    
    prompt = f"""
    Você é um advogado especializado em direito brasileiro. Analise o seguinte documento jurídico e:
    - Resuma os principais pontos do documento.
    - Explique os aspectos legais relevantes.
    - Sugira os próximos passos com base na legislação brasileira.

    Documento:
    """ + texto

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        return f"Erro ao acessar OpenAI: {str(e)}"

# Garantir que o módulo possa ser importado corretamente
__all__ = ["interpretar_movimentacoes", "interpretar_documento"]