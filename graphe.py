import turtle as tu
import task as t


class graphe():
    def __init__(self, lines):
        self.lines = lines
        self.graph = []
        self.create_graph()

    def set_link_value(self, task: t.task):
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
            if any(task.name == line_read[0] for task in self.graph):
                # La tâche a déjà été créée, on passe à la prochaine ligne
                continue
            a = t.task(line_read[0], line_read[1])
            self.graph.append(a)
            if len(line_read) == 2:
                cpt += 1
                a.set_dependencies(entry_node)
        for line in self.lines:
            line_read = line.split()
            a = next(task for task in self.graph if task.name == line_read[0])
            task_read = []
            for element in line_read[2:]:
                task_read.append(int(element))
            for i in task_read:
                for task in self.graph:
                    if task.name == str(i):
                        a.set_dependencies(task)
                        break
            self.set_link_value(a)
        if cpt <= 1:
            self.graph.pop(0)
        exit_nodes = [node for node in self.graph if not any(node in task.dependencies for task in self.graph)]
        exit_task = t.task(len(self.graph), 0)
        for node in exit_nodes:
            print(node.name)
            exit_task.set_dependencies(node)
            exit_task.duration[node.name] = node.out_link
        self.graph.append(exit_task)

    def print_graph(self):
        for task in self.graph:
            for dependencie in task.dependencies:
                print(dependencie.name, '->', task.name, "=", task.duration[dependencie.name])

    def print_matrice(self):
        print("Matrice des valeurs")

        # Calculate the maximum length of task names
        max_length = max([len(str(task.name)) for task in self.graph])

        # Print header row
        header_format = "{:>" + str(max_length) + "}"
        print(header_format.format(""), end=" ")
        for i in range(len(self.graph)):
            print(header_format.format(i), end=" ")
        print()

        # Print each row
        for task in self.graph:
            print(header_format.format(task.name), end=" ")
            for j in range(len(self.graph)):
                if task in self.graph[j].dependencies:
                    print(header_format.format(self.graph[j].duration[task.name]), end=" ")
                else:
                    print(header_format.format("*"), end=" ")
            print()

    def verify_cycle(self):
        graphe_copy = self.graph.copy()
        path = []
        while True:
            print("ITERATION")
            entry_nodes = [node for node in graphe_copy if not node.dependencies]
            for node in entry_nodes:
                if node in path:
                    print("Cycle")
                    return
                print("entry node", node.name)
                graphe_copy.remove(node)
                for node_rank in self.graph:
                    if node_rank in graphe_copy:
                        node_rank.rank += 1
                for task in graphe_copy:
                    if node in task.dependencies:
                        task.dependencies.remove(node)
                        path.append(node)
            if not entry_nodes:
                if graphe_copy:
                    print("Cycle")
                    return
                print("No cycle")
                break



    def print_rank(self):
        print("Rang des tâches")
        for task in self.graph:
            print(task.name, ":", task.rank)

