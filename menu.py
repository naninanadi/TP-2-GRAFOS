import time
import networkx as nx
import matplotlib.pyplot as plt
import gcol

def EscolhaAcao(G,inicio):
    
    escolha = int(input(
        "Digite:\n"
        "1 - Para escolher como colorir o grafo\n"
        "2 - Para imprimir o grafo\n"
        "3 - Para saber o mínimo de cores possível para colorir o grafo\n"
        "4 - Para saber que cor foi atribuída a qual disciplina\n"
        "5 - Finalizar o programa\n"
    ))

    p = {}
    c = gcol.node_precoloring(G, p)

    if escolha == 1:
        c = EscolhaColorimento(G)

    elif escolha == 2:
        EscolhaImpressao(G, c)

    elif escolha == 3:
        print("O número mínimo de cores que pode ser usado é:", gcol.chromatic_number(G))

    elif escolha == 4:
        for vertice, cor in c.items():
            print(f"{vertice} -> Cor {cor}")

    elif escolha == 5:
        fim = time.time()
        print("Tempo aproximado de execução:", round(fim - inicio, 4), "segundos")

    else:
        print("Opção inválida. Nenhuma ação realizada.")

    return escolha

def EscolhaColorimento(G):
    
    escolha = int(input(
        "Escolha o algoritmo de coloração:\n"
        "1 - node_coloring (heurístico)\n"
        "2 - node_coloring (modo exato - opt_alg=1)\n"
        "3 - node_k_coloring (TabuCol)\n"
        "4 - equitable_node_k_coloring\n"
        "5 - node_precoloring\n"
    ))

    p = {}
    c = gcol.node_precoloring(G, p)

    if(escolha == 1):
        c = gcol.node_coloring(G)  
    elif(escolha == 2):
        c = gcol.node_coloring(G, opt_alg=None)  
    elif(escolha == 3):
        k = len(G.nodes())
        c = gcol.node_k_coloring(G, k)  
    elif(escolha == 4):
        k = int(input("Digite o número máximo de cores (k): "))
        c = gcol.equitable_node_k_coloring(G, k) 
    elif(escolha == 5):
        return c
    else:
        print("Opção inválida. Usando coloração heurística por padrão.")
        c = gcol.node_coloring(G)
    
    return c

def EscolhaImpressao(G, c):
        
        escolha = int(input("De que forma gostaria de imprimir o grafo?\n"
                            "1 - Distribuído normalmente\n"
                            "2- Agrupado por cor\n"
                            "3 - Em circulo\n"))
        
        if escolha == 1:
            nx.draw_networkx(G,
                        pos=nx.spring_layout(G, seed=1),
                        node_color=gcol.get_node_colors(G, c))
            plt.show()
        elif escolha == 2:
            nx.draw_networkx(G,
                    pos=gcol.multipartite_layout(G, c),
                    node_color=gcol.get_node_colors(G, c))
            plt.show()
        elif escolha == 3:
            nx.draw_networkx(G,
                 pos=gcol.coloring_layout(G, c),
                 node_color=gcol.get_node_colors(G, c),
                 node_size=20,
                 with_labels=False,
                 width=0.25)
            plt.show()
        else:
             print("Opção indisponível.")
