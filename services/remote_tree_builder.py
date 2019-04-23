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

    def __add_file(self, parent, level, file_id):
        remote_thing = self.google_drive_service.find_file_by_id(file_id)
        new_file = TreeElement(
            level=level,
            relative_path=parent.relative_path + os.sep + remote_thing.name,
            parent=parent,
            childrens=[],
            thing=remote_thing
        )
        self.elements[new_file.relative_path] = new_file
        parent.childrens.append(new_file)

    def add_folder(self, parent, level, folder_id):
        remote_thing = self.google_drive_service.find_file_by_id(folder_id)
        new_folder = TreeElement(
            level=level,
            relative_path=parent.relative_path + os.sep + remote_thing.name,
            parent=parent,
            childrens=[],
            thing=remote_thing
        )
        self.elements[new_folder.relative_path] = new_folder
        parent.childrens.append(new_folder)

    def __create_root_folder(self, root_id):
        # self.root = TreeElement(
        #     level=0,
        #     relative_path='.'+os.sep,
        #     parent=None,
        #     childrens=[],
        #     thing=self.google_drive_service.find_file_by_id(root_id)
        # )
        # self.elements[self.root.relative_path] = self.root
        print(self.google_drive_service.find_files_by_folder_id('root'))

    # def __create_remote_tree(self):

