import os
import sys
from dotenv import load_dotenv

# Ajuste para garantir que o src/ esteja no caminho do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Carregar variáveis do .env
load_dotenv()

# Chaves das APIs
DATAJUD_API_KEY = os.getenv("DATAJUD_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Cabeçalhos para requisições à API Datajud
HEADERS = {
    "Authorization": f"APIKey {DATAJUD_API_KEY}",
    "Content-Type": "application/json"
}

# URLs dos tribunais disponíveis
TRIBUNAIS_URLS = {
    "TRF1": "https://api-publica.datajud.cnj.jus.br/api_publica_trf1/_search",
    "TJDFT": "https://api-publica.datajud.cnj.jus.br/api_publica_tjdft/_search",
    "TJMG": "https://api-publica.datajud.cnj.jus.br/api_publica_tjmg/_search",
    "TJSP": "https://api-publica.datajud.cnj.jus.br/api_publica_tjsp/_search",
    "TJRJ": "https://api-publica.datajud.cnj.jus.br/api_publica_tjrj/_search",
    "TJRS": "https://api-publica.datajud.cnj.jus.br/api_publica_tjrs/_search",
    "TJSC": "https://api-publica.datajud.cnj.jus.br/api_publica_tjsc/_search",
    "TJPR": "https://api-publica.datajud.cnj.jus.br/api_publica_tjpr/_search",
    "TJBA": "https://api-publica.datajud.cnj.jus.br/api_publica_tjba/_search",
    "TJPE": "https://api-publica.datajud.cnj.jus.br/api_publica_tjpe/_search",
}