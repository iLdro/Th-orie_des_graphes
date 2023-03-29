import file_lecture as fl
import graphe as gr
import algo as al


def __main__():
    file = fl.file_lecture('test/table_1')
    graph = gr.graphe(file.file_lines)
    graph.print_graph()
    graph.print_matrice()

    print(al.has_cycle(graph.graph))
    graph.graphism()


if __name__ == "__main__":
    __main__()
