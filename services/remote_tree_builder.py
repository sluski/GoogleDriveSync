from enums.application_consts_enum import ApplicationConstsEnum
from objects.remote_file import RemoteFile
from objects.tree_element import TreeElement
from services.google_drive_service import GoogleDriveService

import os


class RemoteFilesTreeBuilder:

    def __init__(self):
        self.elements = {}
        self.google_drive_service = GoogleDriveService(ApplicationConstsEnum.GOOGLE_API_SCOPE.value, ApplicationConstsEnum.CREDENTIALS_FILE.value)
        self.google_drive_service

    # def __create_root_folder(self, root):
    #     self.root = TreeElement(
    #         level=0,
    #         relative_path='.'+os.sep,
    #         parent=None,
    #         childrends=[],
    #         thing=RemoteFile(
    #             name=root,
    #             type
    #         ))
