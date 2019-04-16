class LocalFile:
    def __init__(self, name, type, location, created, last_modified, md5=None, size=None):
        self.name = name
        self.type = type
        self.location = location
        self.md5 = md5
        self.size = size
        self.created = created
        self.last_modified = last_modified

    def __str__(self):
        result = [
            "Name: {} \n".format(self.name),
            "Type: {} \n".format(self.type),
            "Location: {} \n".format(self.location),
            "MD5: {} \n".format(self.md5),
            "Size: {} \n".format(self.size),
            "Created: {} \n".format(self.created),
            "Last modified: {} \n".format(self.last_modified)
        ]
        return ''.join(result)
