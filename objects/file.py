class File:
    def __init__(self, name, type, location, md5, size, created, last_modified):
        self.name = name
        self.type = type
        self.location = location
        self.md5 = md5
        self.size = size
        self.created = created
        self.last_modified = last_modified
