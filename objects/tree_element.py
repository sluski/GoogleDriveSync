class TreeElement:
    def __init__(self, level, relative_path, parent, childrens, thing):
        self.level = level
        self.parent = parent
        self.childrens = childrens
        self.relative_path = relative_path
        self.thing = thing

    def __str__(self):
        result = [
            "Level: {}, Relative path: {} \n".format(self.level, self.relative_path),
            "Thing: {}".format(self.thing),
        ]
        return ''.join(result)
