from os.path import isfile, isdir
from os import walk, scandir
import os
from enums.file_type_enum import FileTypeEnum
from objects.tree_element import TreeElement
from objects.file import File


class FilesTreeBuilder:

    def __init__(self, root):
        if not isdir(root):
            raise Exception("Root is not folder. Trying set {} as root element".format(root))
        else:
            self.root = TreeElement(
                level=0,
                parent=None,
                childrens=[],
                thing=File(
                    name=root.split("/")[-2],
                    type=FileTypeEnum.FOLDER,
                    location=root,
                    created=os.stat(root).st_ctime,
                    last_modified=os.stat(root).st_mtime))

    def add_folder(self, folder, parent):
        pass
        # folder = TreeElement(
        #     level=parent + 1,
        #     parent=parent,
        #     childrens=[],
        #     thing=File(
        #         name=folder.split,
        #         type=FileTypeEnum.FOLDER,
        #         location=root,
        #         created=os.stat(root).st_ctime,
        #         last_modified=os.stat(root).st_mtime)
        # )
        # folder.level = parent.level + 1
        # folder.
        # parent.childrens.append()

    def add_file(self, file):
        pass


def recur(root):
    for root, dirs, files in walk(root):
        for file in files:
            print("{}/{}".format(root, file))
        for dir in dirs:
            recur(dir)


# recur("/home/sluski/Documents/Laptop/Documents/files")
# def go(path):
#     for a in scandir(path):
#         if a.is_dir():
#             go(a.path)
#         else:
#             print(a.path)

# go('/home/sluski/Documents/Laptop/Documents/files/')

t = FilesTreeBuilder("/home/sluski/Documents/Laptop/Documents/files/")
t.root
print(t.root)

