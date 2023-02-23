class file_lecture():
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(self.file_path, 'r')
        self.file_lines = self.file.readlines()
        self.file.close()

