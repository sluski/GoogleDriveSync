from enums.application_consts_enum import ApplicationConstsEnum
from objects.remote_file import RemoteFile
from objects.tree_element import TreeElement
from services.google_drive_service import GoogleDriveService

import os


class RemoteFilesTreeBuilder:

    def __init__(self, root_id):
        self.elements = {}
        self.google_drive_service = GoogleDriveService(ApplicationConstsEnum.GOOGLE_API_SCOPE.value, ApplicationConstsEnum.CREDENTIALS_FILE.value)
        self.__create_root_folder(root_id)
        self.__create_remote_tree(self.root, self.root.level + 1)

    def __create_remote_tree(self, parent, level):
        for e in self.google_drive_service.find_files_by_folder_id(parent.thing.remote_id):
            if e.is_folder():
                folder = self.__add_folder(parent, level, e)
                self.__create_remote_tree(folder, level+1)
            self.__add_file(parent, level, e)


    def __add_file(self, parent, level, file):
        new_file = TreeElement(
            level=level,
            relative_path=parent.relative_path + os.sep + file.name,
            parent=parent,
            childrens=[],
            thing=file
        )
        self.elements[new_file.relative_path] = new_file
        parent.childrens.append(new_file)
        return new_file

    def __add_folder(self, parent, level, folder):
        new_folder = TreeElement(
            level=level,
            relative_path=parent.relative_path + os.sep + folder.name,
            parent=parent,
            childrens=[],
            thing=folder
        )
        self.elements[new_folder.relative_path] = new_folder
        parent.childrens.append(new_folder)
        return new_folder

    def __create_root_folder(self, root_id):
        self.root = TreeElement(
            level=0,
            relative_path='.',
            parent=None,
            childrens=[],
            thing=self.google_drive_service.find_file_by_id(root_id)
        )
        self.elements[self.root.relative_path] = self.root
