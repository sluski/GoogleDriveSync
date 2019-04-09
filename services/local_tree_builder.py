import os
from os.path import isdir

from commons.common import Common
from enums.file_type_enum import FileTypeEnum
from objects.file import File
from objects.tree_element import TreeElement


class LocalFilesTreeBuilder:

    def __init__(self, root_path):
        self.elements = {}
        if not isdir(root_path):
            raise Exception("Root is not folder. Trying set {} as root element".format(root_path))
        else:
            self.__create_root_element(root_path)
            self.__create_local_tree(root_path)

    def add_folder(self, folder_path):
        parent = self.__find_element_for_path(Common.get_parent_path(folder_path))
        new_folder = TreeElement(
            level=parent.level + 1,
            parent=parent,
            childrens=[],
            thing=File(
                name=Common.extract_name_from_path(folder_path),
                type=FileTypeEnum.FOLDER,
                location=folder_path,
                created=os.stat(folder_path).st_ctime,
                last_modified=os.stat(folder_path).st_mtime)
        )
        parent.childrens.append(new_folder)
        self.elements[folder_path] = new_folder
        return new_folder

    def add_file(self, file_path):
        parent = self.__find_element_for_path(Common.get_parent_path(file_path))
        new_file = TreeElement(
            level=parent.level + 1,
            parent=parent,
            childrens=[],
            thing=File(
                name=Common.extract_name_from_path(file_path),
                type=FileTypeEnum.FILE,
                location=file_path,
                created=os.stat(file_path).st_ctime,
                last_modified=os.stat(file_path).st_mtime,
                md5=Common.generate_md5(file_path),
                size=os.stat(file_path).st_size
            )
        )
        parent.childrens.append(new_file)
        self.elements[file_path] = new_file
        return new_file

    def __create_root_element(self, root_path):
        self.root = TreeElement(
            level=0,
            parent=None,
            childrens=[],
            thing=File(
                name=Common.extract_name_from_path(root_path),
                type=FileTypeEnum.FOLDER,
                location=root_path,
                created=os.stat(root_path).st_ctime,
                last_modified=os.stat(root_path).st_mtime))
        self.elements = {self.root.thing.location: self.root}

    def __create_local_tree(self, path):
        for entry in os.scandir(path):
            if os.path.isdir(entry.path):
                self.add_folder(entry.path)
                Common.get_parent_path(entry.path)
            elif os.path.isfile(entry.path):
                self.add_file(entry.path)

    def __find_element_for_path(self, path):
        return self.elements.get(path)

