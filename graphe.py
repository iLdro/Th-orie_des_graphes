import turtle as tu
import task as t


class graphe():
    def __init__(self, lines):
        self.lines = lines
        self.graph = []
        self.create_graph()

    def set_link_value(self, task : t.task):
        if task.dependencies == '0':
            task.duration['0'] = 0
        else:
            for dependencie in task.dependencies:
                task.duration[dependencie.name] = dependencie.out_link
    def create_graph(self):
        entry_node = t.task('0', 0)
        self.graph.append(entry_node)
        cpt = 0
        for line in self.lines:
            line_read = line.split()
            a = t.task(line_read[0], line_read[1])
            if a not in self.graph:
                self.graph.append(a)
                if len(line_read) == 2:
                    cpt += 1
                    a.set_dependencies(entry_node)
            for i in range(2, len(line_read)):
                for task in self.graph:
                    if task.name == line_read[i]:
                        a.set_dependencies(task)
                        break
            self.set_link_value(a)
        if cpt <= 1:
            self.graph.pop(0)

    def print_graph(self):
        print(len(self.graph))
        for task in self.graph:
            for dependencie in task.dependencies:
                print(dependencie.name, '->', task.name, "=", task.duration[dependencie.name])

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
        for i in range(1,len(self.graph)+1):
            print(i, end=" ")
        print()
        for task in self.graph:
            print(task.name, end="  ")
            for j in range(len(self.graph)):
                if task in self.graph[j].dependencies:
                    print(self.graph[j].duration[task.name], end=" ")
                else:
                    print("*", end=" ")
            print("\n")

    def graphism(self):
        """Draw the graph"""
        for i in range(len(self.graph)):
            tu.penup()
            tu.goto(i * 100, 0)
            tu.pendown()
            tu.write(self.graph[i].name)
            for j in range(len(self.graph)):
                if str(i) in str(self.graph[j].dependencies):
                    tu.penup()
                    tu.goto(i, i)
                    tu.pendown()
                    tu.goto(j, j)
                    tu.write(self.graph[j].duration)
        tu.mainloop()
