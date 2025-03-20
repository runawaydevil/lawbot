import sys
import os
import fitz  # PyMuPDF

# Força a saída padrão para UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Ajuste para garantir que o src/ esteja no caminho do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.openai_interpreter import interpretar_documento

def extrair_texto_pdf(caminho_pdf):
    """Extrai o texto de um arquivo PDF e garante que a codificação esteja correta."""
    try:
        doc = fitz.open(caminho_pdf)
        texto = "\n".join([page.get_text("text") for page in doc])
        texto = texto.encode('latin1', 'ignore').decode('utf-8', 'ignore')  # Corrige caracteres inválidos
        texto = texto.replace('\ufeff', '')  # Remove caracteres BOM UTF-8, se existirem
        return texto.strip() if texto else "O PDF não contém texto extraível."
    except Exception as e:
        return f"Erro ao processar o PDF: {str(e)}"

def verificar_contexto_juridico(texto):
    """Verifica se o documento contém termos jurídicos para definir se é relevante."""
    termos_juridicos = ["ação", "réu", "autor", "processo", "sentença", "juiz", "tribunal", "acórdão", "decisão", "recurso", "lei", "advogado", "contrato", "litígio", "penal", "civil", "cível", "direito"]
    return any(termo.lower() in texto.lower() for termo in termos_juridicos)

def processar_pdf(caminho_pdf):
    """Processa um PDF e gera a interpretação da IA apenas se for jurídico."""
    texto_extraido = extrair_texto_pdf(caminho_pdf)
    
    # Adicionando depuração para verificar o texto antes da IA
    print("🔍 Texto extraído do PDF:")
    print(texto_extraido)
    
    if "Erro ao processar" in texto_extraido or "não contém texto extraível" in texto_extraido:
        return texto_extraido
    
    if not verificar_contexto_juridico(texto_extraido):
        return "⚠️ O documento enviado não parece ser de contexto jurídico. Por favor, envie um documento relacionado ao direito."
    
    resultado_interpretacao = interpretar_documento(texto_extraido)
    
    # Adicionando depuração para verificar o texto interpretado
    print("🧠 Resumo gerado pela IA:")
    print(resultado_interpretacao)
    
    return resultado_interpretacao

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python pdf_processor.py <caminho_do_pdf>")
        sys.exit(1)
    
    caminho_pdf = sys.argv[1]
    resultado = processar_pdf(caminho_pdf)
    print(resultado)
