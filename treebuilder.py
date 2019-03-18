from os import *
from os.path import isfile


class TreeBuilder:

    def __init__(self, root_path):
        if isfile(root_path):
            raise Exception("Root is not folder. Trying set {} as root element".format(root_path))
        else:
            self.root_path = root_path

    def add_folder(self, name, location, created, last_modified):


tree = TreeBuilder("/home/sluski/Documents/files/test.txt")
