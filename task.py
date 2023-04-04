class task():
    def __init__(self, name, out_link=0):
        self.name = name
        self.duration = {}
        self.dependencies = []
        self.out_link = int(out_link)
        self.rank = 0

    def set_dependencies(self, dependencie):
        self.dependencies.append(dependencie)

