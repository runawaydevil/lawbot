import os
import sys
from datetime import datetime

# Ajuste para garantir que o src/ esteja no caminho do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from api_datajud import consultar_processo, consultar_em_todos_tribunais
from openai_interpreter import interpretar_movimentacoes

def formatar_data(data_str):
    """Converte a data para um formato legível."""
    try:
        return datetime.strptime(data_str, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%d/%m/%Y %H:%M")
    except:
        return data_str

def organizar_movimentacoes(movimentacoes):
    """Ordena e formata as movimentações processuais, removendo movimentações irrelevantes."""
    movimentacoes.sort(key=lambda x: x.get("dataHora", ""), reverse=True)
    
    # Lista de movimentações que queremos ignorar
    ignorar_movimentacoes = {"Mero expediente", "Decurso de Prazo"}

    eventos_unicos = {}
    
    for mov in movimentacoes:
        descricao = mov.get("nome", "Movimentação desconhecida")

        # Se a movimentação está na lista de ignorados, não adicionamos
        if descricao in ignorar_movimentacoes:
            continue
        
        data = formatar_data(mov.get("dataHora", "Data desconhecida"))
        
        if descricao not in eventos_unicos:
            eventos_unicos[descricao] = []
        eventos_unicos[descricao].append(data)
    
    if not eventos_unicos:
        return "📌 Nenhuma movimentação relevante foi encontrada.\n"

    resposta = "\n📜 **Histórico das Movimentações Recentes:**\n"
    for descricao, datas in eventos_unicos.items():
        resposta += f"- 📌 {descricao}: {', '.join(datas)}\n"
    
    return resposta

def main():
    print("\n📌 Consulta Processual Jurídica - Datajud\n")
    sys.stdout.flush()
    
    while True:
        try:
            print("Digite o número do processo:")
            sys.stdout.flush()
            numero_processo = input().strip()
            
            print("Digite o código do tribunal (ou pressione ENTER para pesquisar em todos):")
            sys.stdout.flush()
            tribunal = input().strip().upper()
            
            if tribunal:
                dados_processo = consultar_processo(tribunal, numero_processo)
            else:
                dados_processo = consultar_em_todos_tribunais(numero_processo)

            if dados_processo and "hits" in dados_processo.get("hits", {}):
                resultados = dados_processo["hits"]["hits"]
                
                if resultados:
                    detalhes = resultados[0]["_source"]
                    print("\n🔎 **Detalhes do Processo:**")
                    print(f"📌 Número: {detalhes.get('numeroProcesso')}")
                    print(f"📍 Tribunal: {detalhes.get('tribunal')}")
                    print(f"📅 Ajuizamento: {formatar_data(detalhes.get('dataAjuizamento', 'Data desconhecida'))}")
                    print(f"📂 Classe Processual: {detalhes['classe']['nome']}")
                    print(f"⚖️ Órgão Julgador: {detalhes.get('orgaoJulgador', {}).get('nome', 'Desconhecido')}")
                    
                    print(organizar_movimentacoes(detalhes.get("movimentos", [])))
                    
                    print("\n⚖️ **Interpretando Movimentações...**")
                    resumo = interpretar_movimentacoes(
                        detalhes.get("movimentos", []), 
                        detalhes.get("numeroProcesso"), 
                        detalhes.get("tribunal")
                    )
                    print(resumo)
                else:
                    print("\n❌ Nenhum processo encontrado com esse número.")
            else:
                print("\n❌ Erro na consulta.")
            
            sys.stdout.flush()
        except EOFError:
            break

if __name__ == "__main__":
    main()