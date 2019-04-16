from enums.application_consts_enum import ApplicationConstsEnum
from objects.tree_element import TreeElement
from services.google_drive_service import GoogleDriveService


class RemoteFilesTreeBuilder:

    def __init__(self):
        self.elements = {}
        self.google_drive_service = GoogleDriveService(ApplicationConstsEnum.GOOGLE_API_SCOPE.value, ApplicationConstsEnum.CREDENTIALS_FILE.value)

    def __create_root_folder(self, root):
        self.root = TreeElement(0, )
