
import task as t
class graphe():
    def __init__(self, lines):
        self.lines = lines
        self.graph = []
        self.create_graph()


    def create_graph(self):
        for line in self.lines:
            line_read=line.split()
            a = t.task(line_read[0], line_read[1])
            if a not in self.graph:
                self.graph.append(a)
                if len(line_read) == 2:
                    a.set_dependencies('0')
            for i in range(2, len(line_read)):
                a.set_dependencies(line_read[i])

    def print_graph(self):
        for task in self.graph:
            for dependencie in task.dependencies:
                print(dependencie, '->', task.name,"=", task.duration)


    def print_matrice(self):
        """Matrice des valeurs
                               0 1 2 3 4 5 6
                              0 * 0 0 * * * *
                              1 * * * 1 1 * *
                              2 * * * * 2 2 *
                              3 * * * * * * 3
                              4 * * * * * 4 *
                              5 * * * * * * 5
                              6 * * * * * * *"""
        print("Matrice des valeurs")
        print(" ", end="")
        for i in range(len(self.graph)):
            print(i, end=" ")
        print()
        for i in range(len(self.graph)):
            print(i, end="  ")
            for j in range(len(self.graph)):
                if str(i) in str(self.graph[j].dependencies):
                    print(self.graph[j].duration, end=" ")
                else :
                    print("*", end=" ")
            print("\n")





