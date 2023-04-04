class task():
    def __init__(self, name, out_link=0):
        self.name = name
        self.duration = {}
        self.dependencies = []
        self.out_link = int(out_link)
        self.rank = 0
        self.children = []
        self.early_start = 0
        self.late_start = 0


    def get_children(self, tasks):
        return list(filter(lambda t: self in t.dependencies, tasks))

    def set_dependencies(self, dependencie):
        self.dependencies.append(dependencie)
