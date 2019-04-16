class TreeElement:
    def __init__(self, level, relative_path, parent, childrens, thing):
        self.level = level
        self.parent = parent
        self.childrens = childrens
        self.relative_path = relative_path
        self.thing = thing

    def __str__(self):
        result = [
            "\n> Thing:\n{} \n".format(self.thing),
            "> Level: {} \n".format(self.level),
            "> Relative path: {} \n".format(self.relative_path),
            "> Parent: {} \n".format(self.parent),
            "> Childrens: {} \n".format(self.childrens)
        ]
        return ''.join(result)
