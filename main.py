import networkx as nx
import matplotlib.pyplot as plt
import gcol

def LeituraArquivo(NomeArquivo):
    arq = open(NomeArquivo)
    linhas = arq.readlines()
    x = 0
    while x < len(linhas):
        if linhas[x] == "\n":
            local = linhas.index(linhas[x])
            linhas.pop(local)
        else:
            linhas[x] = linhas[x].split(',')
            x += 1

    for i in linhas:
        local = linhas.index(i) 
        for b in i:
            local2 = linhas[local].index(b) 
            if "\n" in b:
                linhas[local][local2] = b.replace("\n",'')
    return linhas



def main():
    NomeArquivo = input("Digite o nome do arquivo formatado: ")
    try:
        linhas = LeituraArquivo(NomeArquivo)
        
        # Set porque não vai permitir repetição
        Vertices = set()

        #Vai virar uma matriz
        Ligacoes = []

        for linha in linhas:
            if len(linha) >= 2:
                Vertices.add(linha[0])
                Vertices.add(linha[1])
                Ligacoes.append(linha)
        
        # Grafo começa vazio
        G = nx.Graph()

        # Ordena os vértices em ordem alfabética, pra que A -> 0, B -> 1
        Vertices = sorted(Vertices)

        # Faz um dicionário que mapeia A:0, B:1 e por ai vai
        mapa_indices = {v: i for i, v in enumerate(Vertices)}

        # Na matriz de Ligações, sempre que A aparecer, muda pra 0, sempre que B aparecer, muda pra 1 e por ai vai
        Ligacoes = [[mapa_indices[a], mapa_indices[b]] for a, b in Ligacoes]

        # Adiciona arestas a partir dos vértices (quando eles não existem, a função já adiciona automaticamente)
        for lig in Ligacoes:
            G.add_edges_from([(lig[0], lig[1])])

        # Colore o grafo, usando o menor número de cores possível
        c = gcol.node_coloring(G)

        # Mostra os horários
        print("O número mínimo de cores usado foi:", max(c.values()) + 1)

        # Imprime o grafo de duas formas diferentes
        # print("Here is a picture of this coloring:")
        # nx.draw_networkx(G,
        #                 pos=nx.spring_layout(G, seed=1),
        #                 node_color=gcol.get_node_colors(G, c))
        # plt.show()

        # nx.draw_networkx(G,
        #          pos=gcol.multipartite_layout(G, c),
        #          node_color=gcol.get_node_colors(G, c))
        # plt.show()
     
    except FileNotFoundError:
        print(f"Erro: Arquivo '{NomeArquivo}' não encontrado!")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()