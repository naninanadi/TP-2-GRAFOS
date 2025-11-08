import time
import networkx as nx
import matplotlib.pyplot as plt
import gcol
import entrada
import menu

def main():
    NomeArquivo = input("Digite o nome do arquivo formatado: ")
    try:

        NomeArquivo = "Entradas/" + NomeArquivo
        linhas = entrada.LeituraArquivo(NomeArquivo)

        escolha = 0

        while escolha != 5:
            inicio = time.time()

            # Grafo começa vazio
            G = nx.Graph()

            # Adiciona as ligações, que representam os conflitos
            for linha in linhas:
                if len(linha) >= 2 and linha[0] != "Disciplina1":
                    G.add_edges_from([(linha[0], linha[1])])
            
            # Colore o grafo, usando o menor número de cores possível
            escolha = menu.EscolhaAcao(G, inicio)

     
    except FileNotFoundError:
        print(f"Erro: Arquivo '{NomeArquivo}' não encontrado!")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()