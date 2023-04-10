class task():
    def __init__(self, name, out_link=0):
        self.name = name
        self.duration = {name: 0}
        self.dependencies = []
        self.children = []
        self.out_link = int(out_link)
        self.rank = 0
        self.early_date = 0
        self.late_date = 0


    def set_dependencies(self, dependencie):
        self.dependencies.append(dependencie)

