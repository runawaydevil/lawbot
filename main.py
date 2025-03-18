from api_datajud import consultar_processo, consultar_em_todos_tribunais
from openai_interpreter import interpretar_movimentacoes

def main():
    print("\n📌 Consulta Processual Jurídica - Datajud\n")

    numero_processo = input("Digite o número do processo: ")
    tribunal = input("Digite o código do tribunal (ou pressione ENTER para pesquisar em todos): ").upper()

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
            print(f"📅 Ajuizamento: {detalhes.get('dataAjuizamento')}")
            print(f"📂 Classe Processual: {detalhes['classe']['nome']}")

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

if __name__ == "__main__":
    main()
