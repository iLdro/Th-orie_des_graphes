import graphe as gr
from copy import deepcopy
import sys
import os
import file_lecture as fl


class tracegenerator :
    def __init__(self):
        self.files = sorted(os.listdir("test"), key=lambda x: int(x.split('_')[-1]))
        for i in range(1, len(self.files) + 1):
            file = fl.file_lecture('test/' + self.files[i - 1])
            graph = gr.graphe(file.file_lines)
            open(f"trace/test-{self.files[i - 1].split('_')[-1]}.txt", 'a').close()
            with open(f"trace/test-{self.files[i - 1].split('_')[-1]}.txt", 'w', encoding='UTF-8') as f:
                f.write("Lancement du programme pour le fichier : table_" + str(i) + "\n")
                sys.stdout = f
                print("affichage du graphe sous forme de lignes")
                graph.print_graph()
                print('\n')
                print("affichage du graphe sous forme de matrice")
                graph.print_matrice()
                print('\n')
                print("Vérification de l'ordenancement")
                print("Le graphe possède-t-il des cycles")
                graph_copy = deepcopy(graph)
                cycle = graph_copy.verify_cycle()
                print("Le graphe a-t-il des valeurs négatives")
                negative = graph.check_negaive_value()
                if negative and cycle:
                    print("Il s'agit d'un graphe d'ordonnecement")
                    ordo_check = 1
                else:
                    print("Il ne s'agit pas d'une graphe d'ordonnecement")
                    ordo_check = 0

                print('\n')
                if ordo_check == 1:
                    graph_copy = deepcopy(graph)
                    graph_copy.set_rank()
                    for i in range(len(graph_copy.graph)):
                        graph.graph[i].rank = graph_copy.graph[i].rank
                    print("Affichage du rang de chaque tâche")
                    graph.print_rank()
                    print('\n')
                    graph.calculate_early_start()
                    print("Affichage de la date au plus tôt")
                    graph.display_early_start()
                    print('\n')
                    graph.compute_late_start()
                    print("Affichade de la date au plus tard")
                    graph.display_late_start()
                    print('\n')
                    print("Affichage des marges")
                    graph.compute_margins()
                    print('\n')
                    print("Affichage du chemin critique")
                    graph.display_critical_path()


