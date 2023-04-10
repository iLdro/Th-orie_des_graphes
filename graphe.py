import turtle as tu
import task as t
from prettytable import PrettyTable


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
        for line in self.lines:
            line_read = line.split()
            if any(task.name == line_read[0] for task in self.graph):
                continue
            a = t.task(line_read[0], line_read[1])
            self.graph.append(a)
            if len(line_read) == 2:
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
        exit_nodes = [node for node in self.graph if not any(node in task.dependencies for task in self.graph)]
        exit_task = t.task(len(self.graph), 0)
        for node in exit_nodes:
            exit_task.set_dependencies(node)
            exit_task.duration[node.name] = node.out_link
        self.graph.append(exit_task)

    def print_graph(self):
        for task in self.graph:
            for dependencie in task.dependencies:
                print(dependencie.name, '->', task.name, "=", task.duration[dependencie.name])

    def print_matrice(self):
        print("Matrice des valeurs pour le graphe :")

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

    def set_rank(self):
        if self.graph[-1].rank !=0:
            pass
        else:
            graphe_copy = self.graph.copy()
            path = []
            while True:
                entry_nodes = [node for node in graphe_copy if not node.dependencies]
                node_ranked_update = []
                for node in entry_nodes:
                    if node in path:
                        return graphe_copy
                    graphe_copy.remove(node)
                    for node_rank in self.graph:
                        if node_rank in graphe_copy and node_rank not in entry_nodes:
                            node_ranked_update.append(node_rank)
                    for task in graphe_copy:
                        if node in task.dependencies:
                            task.dependencies.remove(node)
                            path.append(node)
                if not entry_nodes:
                    if graphe_copy:
                        return graphe_copy
                    return graphe_copy
                node_ranked_update = list(set(node_ranked_update))
                for update in node_ranked_update:
                    update.rank += 1

    def verify_cycle(self):
        graphe_copy = self.graph.copy()
        path = []
        while True:
            print("\n")
            entry_nodes = [node for node in graphe_copy if not node.dependencies]
            print("Nouveau point d'entrée :", end=" ")
            for node in entry_nodes:
                print(node.name, end=" ")
                if node in path:
                    print("Le graphe contient un cycle")
                    return False
                graphe_copy.remove(node)
                for task in graphe_copy:
                    if node in task.dependencies:
                        task.dependencies.remove(node)
                        path.append(node)
            if not entry_nodes:
                if graphe_copy:
                    print("Le graphe contient un cycle")
                    return False
                print("Le graphe ne contient pas de cycle")
                return True

    def check_negaive_value(self):
        for task in self.graph:
            for dependencie in task.dependencies:
                if task.duration[dependencie.name] < 0:
                    print("Le graphe contient une valeur négative")
                    return False
        print("Le graphe ne contient pas de valeur négative")
        return True

    def print_rank(self):
        print("Rang des tâches")
        for task in self.graph:
            print(task.name, ":", task.rank)

    def order_by_rank(self):
        rank_order = []

        for task in self.graph:
            rank_order.append(task.rank)
        rank_order = list(set(rank_order))
        rank_order.sort()
        task_by_rank = []
        for rank in rank_order:
            task_by_rank.append([task for task in self.graph if task.rank == rank])
        return task_by_rank

    def calculate_early_start(self):
        task_by_rank = self.order_by_rank()
        for i in range(len(task_by_rank)):
            for j in task_by_rank[i]:
                if i == 0:
                    for task in self.graph:
                        if task == j:
                            task.early_date = 0
                else:
                    for task in self.graph:
                        if task == j:
                            task.early_date = max(
                                [task.duration[dependencie.name] + dependencie.early_date for dependencie in
                                 task.dependencies])

    def display_early_start(self):
        table = PrettyTable()
        table.field_names = ["Tâche", "Début précoce"]
        for task in self.graph:
            table.add_row([task.name, task.early_date])
        print(table)

    def set_child_to_task(self):
        for task in self.graph:
            for t in self.graph:
                if task in t.dependencies:
                    task.children.append(t)

    def compute_late_start(self):
        self.set_child_to_task()
        self.calculate_early_start()
        task_by_rank = self.order_by_rank()
        task_by_rank.reverse()
        for i in range(len(task_by_rank)):
            for j in task_by_rank[i]:
                if i == 0:
                    for task in self.graph:
                        if task == j:
                            task.late_date = task.early_date
                else:
                    for task in self.graph:
                        if task == j:
                            possible_latedate = []
                            for child in task.children:
                                possible_latedate.append(child.late_date - task.out_link)
                            print()
                            task.late_date = min(possible_latedate)



    def display_late_start(self):
        table = PrettyTable()
        table.field_names = ["Tâche", "Début tardif abs"]

        for task in self.graph:
            table.add_row([task.name, task.late_date])
        print(table)

    def compute_margins(self):
        table = PrettyTable()
        table.field_names = ["Tâche", "Marge totale"]
        for task in self.graph:
            table.add_row([task.name, task.late_date - task.early_date])
        print(table)

    def compute_critical_path(self):
        #Get all the task wwhich have a margin of 0 and 0 as dependencies
        critical_path = []
        entries_node= []
        entry_node = [node for node in self.graph if not node.dependencies]
        exit_node = [node for node in self.graph if not node.children]
        for task in self.graph:
            if task.late_date - task.early_date == 0 and entry_node[0] in task.dependencies:
                entries_node.append(task)

        while entries_node:
            node_treated = entries_node.pop()
            print(node_treated.name)
            critical_path.append([node_treated])
            while critical_path[-1][-1] not in exit_node:
                for task in self.graph:
                    if task.late_date - task.early_date == 0 and critical_path[-1][-1] in task.dependencies:
                        critical_path[-1].append(task)
        for i in range(len(critical_path)):
            critical_path[i].insert(0, entry_node[0])

        if len(critical_path) > 1:
            print("Chemins critiques  possibles:")
            for path in critical_path:
                for node in path:
                    print(node.name, end=" ")
                print("\n")
        # on prend le/les chemin(s) dont la durée est la plus grande
        max_duration = 0
        longest_path = None

        for path in critical_path:
            path_duration = sum([node.out_link for node in path])

            if path_duration > max_duration:
                max_duration = path_duration
                longest_path = path

        return longest_path

    def display_critical_path(self):
        critical_path = self.compute_critical_path()
        print("Chemin critique")
        for node in critical_path:
            print(node.name, end=" ")
