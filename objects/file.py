class File:
    def __init__(self, name, type, created, md5, size):
        self.name = name
        self.type = type
        self.md5 = md5
        self.size = size
        self.created = created
