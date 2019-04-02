import hashlib
import os
from os.path import isdir

from enums.file_type_enum import FileTypeEnum
from objects.file import File
from objects.tree_element import TreeElement


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
            self.__elementes = {self.root.thing.location: self.root}

    def add_folder(self, folder_path, parent):
        new_folder = TreeElement(
            level=parent.level + 1,
            parent=parent,
            childrens=[],
            thing=File(
                name=self.__extract_name_from_path(folder_path),
                type=FileTypeEnum.FOLDER,
                location=folder_path,
                created=os.stat(folder_path).st_ctime,
                last_modified=os.stat(folder_path).st_mtime)
        )
        parent.childrens.append(new_folder)
        self.__elementes[folder_path] = new_folder
        return new_folder

    def add_file(self, file_path, parent):
        new_file = TreeElement(
            level=parent.level + 1,
            parent=parent,
            childrens=[],
            thing=File(
                name=self.__extract_name_from_path(file_path),
                type=FileTypeEnum.FILE,
                location=file_path,
                created=os.stat(file_path).st_ctime,
                last_modified=os.stat(file_path).st_mtime,
                md5=self.__generate_file_md5(file_path),
                size=os.stat(file_path).st_size
            )
        )
        parent.childrens.append(new_file)
        self.__elementes[file_path] = new_file
        return new_file

    @staticmethod
    def __generate_file_md5(file_path):
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    @staticmethod
    def __extract_name_from_path(path):
        return path.split("/")[-2]

    def find_element_for_path(self, path):
        return self.__elementes.get(path)
