class task():
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.dependencies = []

    def set_dependencies(self, dependencie):
        self.dependencies.append(dependencie)