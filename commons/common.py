class Pair:

    def __init__(self, first, second):
        self.first = first
        self.second = second


class Map:

    def __init__(self, key, value):
        self.key = key
        self.value = value


class File:

    def __init__(self, name, md5, additional={}):
        self.name = name
        self.md5 = md5
        self.additional = additional

    def return_as_dict(self):
        return {'name': self.name, 'md5': self.md5, 'additional': self.additional}
