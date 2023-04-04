import file_lecture as fl
import graphe as gr
import algo as al
from copy import deepcopy


def __main__():
    file = fl.file_lecture('test/table_3')
    graph = gr.graphe(file.file_lines)
    graph.print_graph()
    graph.print_matrice()
    # Créer une copie du graph
    graph_copy = deepcopy(graph)
    graph_copy.verify_cycle()
    graph_copy.print_rank()
    graph.print_graph()




if __name__ == "__main__":
    __main__()
