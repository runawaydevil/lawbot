import requests
import re
from config import HEADERS, TRIBUNAIS_URLS
from rich import print_json

def formatar_numero_processo(numero_processo: str) -> str:
    """Remove pontos e hífens do número do processo."""
    return re.sub(r'\D', '', numero_processo)  # Remove tudo que não for número

def consultar_processo(tribunal: str, numero_processo: str):
    """Consulta um processo na API do Datajud em um tribunal específico."""
    numero_processo = formatar_numero_processo(numero_processo)  # Formata o número antes de enviar
    
    url = TRIBUNAIS_URLS.get(tribunal.upper())
    if not url:
        print("[red]❌ Tribunal não encontrado.[/red]")
        return None
    
    payload = {
        "query": {
            "match": {
                "numeroProcesso": numero_processo
            }
        }
    }
    
    response = requests.post(url, headers=HEADERS, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        if data["hits"]["total"]["value"] > 0:
            print_json(data=data)  # Exibe os dados formatados
            return data
    return None

def consultar_em_todos_tribunais(numero_processo: str):
    """Consulta um processo em todos os tribunais até encontrar um resultado."""
    numero_processo = formatar_numero_processo(numero_processo)  # Formata o número antes de enviar
    
    print("\n🔎 Buscando o processo em todos os tribunais...")
    
    for tribunal, url in TRIBUNAIS_URLS.items():
        print(f"📍 Consultando no tribunal: {tribunal}...")
        
        payload = {
            "query": {
                "match": {
                    "numeroProcesso": numero_processo
                }
            }
        }
        
        response = requests.post(url, headers=HEADERS, json=payload)
        
        if response.status_code == 200:
            data = response.json()
            if data["hits"]["total"]["value"] > 0:
                print(f"\n✅ Processo encontrado no tribunal: {tribunal}")
                print_json(data=data)
                return data  # Retorna o primeiro resultado encontrado
    
    print("\n❌ Nenhum processo encontrado em nenhum tribunal.")
    return None