class TreeElement:
    def __init__(self, level, parent, childrens, thing):
        self.level = level
        self.parent = parent
        self.childrens = childrens
        self.thing = thing

    def __str__(self):
        result = [
            "Level: {} \n".format(self.level),
            "Parent: {} \n".format(self.parent),
            "Childrens: {} \n".format(self.childrens),
            "\nThing:\n{} \n".format(self.thing)
        ]
        return ''.join(result)
