import os
from os.path import isdir

from commons.common import Common
from enums.file_type_enum import FileTypeEnum
from objects.local_file import LocalFile
from objects.tree_element import TreeElement


class LocalFilesTreeBuilder:

    def __init__(self, root_path):
        self.elements = {}
        if not isdir(root_path):
            raise Exception("Root is not folder. Trying set {} as root element".format(root_path))
        else:
            self.__create_root_element(root_path)
            self.__create_local_tree(root_path, 1)

    def __add_folder(self, folder_path, level):
        parent = self.__find_element_for_relative_path(self.__extract_parent_relative_path(folder_path, level))
        new_folder = TreeElement(
            level=level,
            parent=parent,
            relative_path=parent.relative_path + os.sep + Common.extract_name_from_path(folder_path),
            childrens=[],
            thing=LocalFile(
                name=Common.extract_name_from_path(folder_path),
                type=FileTypeEnum.FOLDER,
                location=folder_path,
                created=os.stat(folder_path).st_ctime,
                last_modified=os.stat(folder_path).st_mtime)
        )
        parent.childrens.append(new_folder)
        self.elements[new_folder.relative_path] = new_folder
        return new_folder

    def __add_file(self, file_path, level):
        parent = self.__find_element_for_relative_path(self.__extract_parent_relative_path(file_path, level))
        new_file = TreeElement(
            level=level,
            parent=parent,
            relative_path=parent.relative_path + os.sep + Common.extract_name_from_path(file_path),
            childrens=[],
            thing=LocalFile(
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
        self.elements[new_file.relative_path] = new_file
        return new_file

    def __create_root_element(self, root_path):
        self.root = TreeElement(
            level=0,
            parent=None,
            relative_path='.',
            childrens=[],
            thing=LocalFile(
                name=Common.extract_name_from_path(root_path),
                type=FileTypeEnum.FOLDER,
                location=root_path,
                created=os.stat(root_path).st_ctime,
                last_modified=os.stat(root_path).st_mtime))
        self.elements = {self.root.relative_path: self.root}

    def __create_local_tree(self, path, level):
        for entry in os.scandir(path):
            if os.path.isdir(entry.path):
                self.__add_folder(entry.path, level)
                self.__create_local_tree(entry.path, level + 1)
            elif os.path.isfile(entry.path):
                self.__add_file(entry.path, level)

    @staticmethod
    def __extract_parent_relative_path(children_full_path, level):
        splited_path = children_full_path.split(os.sep)
        result = '.'
        for e in splited_path[-level:-1]:
            result = result + os.sep + e

        return result

    def __find_element_for_relative_path(self, relative_path):
        return self.elements.get(relative_path)

