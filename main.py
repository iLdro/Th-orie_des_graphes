import file_lecture as fl
import graphe as gr
import algo as al


def __main__():
    file = fl.file_lecture('test/table_4.txt')
    graph = gr.graphe(file.file_lines)
    graph.print_graph()
    graph.print_matrice()

    print(al.has_cycle(graph.graph))


if __name__ == "__main__":
    __main__()
