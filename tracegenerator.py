import graphe as gr
from copy import deepcopy
import sys
import os
import file_lecture as fl


class tracegenerator :
    def __init__(self):
        self.files = os.listdir("test")
        for i in range(1,len(self.files)+1):
            file = fl.file_lecture('test/table_' + str(i))
            self.graph = gr.graphe(file.file_lines)
            open(f"trace/test-{self.files[i - 1].split('_')[-1]}.txt", 'a').close()
            with open(f"trace/test-{self.files[i - 1].split('_')[-1]}.txt", 'w', encoding='UTF-8') as f:
                f.write("Lancement du programme\n")
                sys.stdout = f
                print("affichage du graphe sous forme de lignes")
                self.graph.print_graph()
                print('\n')
                print("affichage du graphe sous forme de matrice")
                self.graph.print_matrice()
                print('\n')
                print("Vérification de l'ordenancement")
                graph_copy = deepcopy(self.graph)
                cycle = graph_copy.verify_cycle()
                print("Le graphe a-t-il des valeurs négatives")
                negative = self.graph.check_negaive_value()
                if negative and cycle:
                    print("Il s'agit d'un graphe d'ordonancement")
                    ordo_check = 1
                else:
                    print("Il ne s'agit pas d'une graphe d'ordonancement")
                    ordo_check = 0

                print('\n')
                if ordo_check == 1:
                    graph_copy = deepcopy(self.graph)
                    graph_copy.set_rank()
                    for i in range(len(graph_copy.graph)):
                        self.graph.graph[i].rank = graph_copy.graph[i].rank
                    print("Affichage du rang de chaque tâche")
                    self.graph.print_rank()
                    print('\n')
                    self.graph.calculate_early_start()
                    print("Affichage de la date au plus tôt")
                    self.graph.display_early_start()
                    print('\n')
                    self.graph.compute_late_start()
                    print("Affichade de la date au plus tard")
                    self.graph.display_late_start()
                    print('\n')
                    print("Affichage des marges")
                    self.graph.compute_margins()
                    print('\n')
                    print("Affichage du chemin critique")
                    self.graph.display_critical_path()


