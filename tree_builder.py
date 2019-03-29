from os.path import isdir
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
                    name=self.__extract_name_from_path(root),
                    type=FileTypeEnum.FOLDER,
                    location=root,
                    created=os.stat(root).st_ctime,
                    last_modified=os.stat(root).st_mtime))

    def add_folder(self, folder_location, parent):
        new_folder = TreeElement(
            level=parent.level + 1,
            parent=parent,
            childrens=[],
            thing=File(
                name=self.__extract_name_from_path(folder_location),
                type=FileTypeEnum.FOLDER,
                location=folder_location,
                created=os.stat(folder_location).st_ctime,
                last_modified=os.stat(folder_location).st_mtime)
        )
        parent.childrens.append(new_folder)

    def add_file(self, file_location, parent):
        new_file = TreeElement(
            level=parent.level + 1,
            parent=parent,
            childrens=[],
            thing=File(
                name=self.__extract_name_from_path(file_location),
                type=FileTypeEnum.FILE,
                location=file_location,
                created=os.stat(file_location).st_ctime,
                last_modified=os.stat(file_location).st_mtime
            )
        )
        parent.childrens.append(new_file)

    @staticmethod
    def __extract_name_from_path(path):
        return path.split("/")[-2]