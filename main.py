import networkx as nx
import matplotlib.pyplot as plt


class ArmazenamentoReagentes:

    def __init__(self):
        self.grafo = nx.Graph()

    def adicionar_reagente(self, reagente):
        self.grafo.add_node(reagente)

    def adicionar_incompatibilidade(self, reagente1, reagente2):
        self.grafo.add_edge(reagente1, reagente2)

    def colorir_galpoes(self):
        coloracao = nx.greedy_color(self.grafo, strategy='largest_first')
        return coloracao

    def visualizar_armazenamento(self):
        cores = [self.coloracao[n] for n in self.grafo.nodes]
        nx.draw(self.grafo,
                with_labels=True,
                node_color=cores,
                cmap=plt.cm.rainbow)
        plt.show()


if __name__ == "__main__":
    armazenamento = ArmazenamentoReagentes()

    num_reagentes = int(input("Quantos reagentes deseja adicionar? "))

    # Adicionar reagentes
    for i in range(num_reagentes):
        reagente = input(f"Informe o nome do reagente {i+1}: ")
        armazenamento.adicionar_reagente(reagente)

    # Adicionar incompatibilidades
    num_incompatibilidades = int(input("Quantas incompatibilidades deseja adicionar? "))
    for i in range(num_incompatibilidades):
        reagente1 = input(f"Informe o nome do primeiro reagente da incompatibilidade {i+1}: ")
        reagente2 = input(f"Informe o nome do segundo reagente da incompatibilidade {i+1}: ")
        armazenamento.adicionar_incompatibilidade(reagente1, reagente2)

    # Colorir galpões e visualizar resultado
    armazenamento.coloracao = armazenamento.colorir_galpoes()
    armazenamento.visualizar_armazenamento()
