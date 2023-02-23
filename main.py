import file_lecture as fl
import graphe as gr

def __main__():
    file = fl.file_lecture('test/table_4.txt')
    graph = gr.graphe(file.file_lines)
    graph.print_graph()
    graph.print_matrice()


if __name__ == "__main__":
    __main__()
