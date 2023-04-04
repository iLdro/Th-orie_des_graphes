import file_lecture as fl
import graphe as gr
import algo as al
from copy import deepcopy


def Affichage():
    while True:
        print("Lancement du programme")
        print("Veuillez choisir un graphe entre 1 et 11")
        while True:
            try:
                graph_number = int(input())
                if graph_number < 1 or graph_number > 11:
                    print("Veuillez choisir un graphe entre 1 et 11")
                else:
                    break
            except ValueError:
                print("Veuillez choisir un graphe entre 1 et 11")
        file = fl.file_lecture('test/table_' + str(graph_number))
        graph = gr.graphe(file.file_lines)
        ordo_check = 0
        print("Que souhaitez-vous faire ?")
        print("0 - EXIT")
        print("1 - Afficher le graphe")
        print("2 - Afficher la matrice des valeurs")
        print("3 - Vérifier s'il s'agit d'un graphe d'ordonnancement")
        print("4 - Afficher le rang de chaque tâche")
        print("5 - Afficher la date au plus tôt")
        print("6 - Afficher la date au plus tard")
        print("7 - Afficher le chemin critique")

        while True:
            choix = int(input("Choisissez un nombre :\n"))
            if choix == 0:
                return
            elif choix == 1:
                print("Affichage sous forme de lignes")
                graph.print_graph()
            elif choix == 2:
                print("Affichage sous forme de matrice")
                graph.print_matrice()
            elif choix == 3:
                print("Le graphe possède-t-il des cycles")
                graph_copy = deepcopy(graph)
                cycle =graph_copy.verify_cycle()
                print("Le graphe a-t-il des valeurs négatives")
                negative = graph.check_negaive_value()
                if negative and cycle:
                    print("Il s'agit d'un graphe d'ordonnecement")
                    ordo_check = 1
                else:
                    print("Il ne s'agit pas d'une graphe d'ordonnecement")
                    ordo_check = 0

            elif choix == 4:
                if ordo_check == 1:
                    graph_copy = deepcopy(graph)
                    graph_copy.set_rank()
                    for i in range(len(graph_copy.graph)):
                        graph.graph[i].rank = graph_copy.graph[i].rank
                    print("Affichage du rang de chaque tâche")
                    graph.print_rank()
                else:
                    print("Le graphe n'est pas un graphe d'ordonnancement nous ne pouvons pas effectuer cette opération")
            elif choix == 5:
                graph.calculate_early_start()
                print("Affichage de la date au plus tôt")
                graph.display_early_start()
            elif choix == 6:
                graph.compute_late_start()
                graph.display_late_start()
            elif choix == 7:
                graph.compute_margins()
