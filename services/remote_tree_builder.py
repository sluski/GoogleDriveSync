from enums.application_consts_enum import ApplicationConstsEnum
from services.google_drive_service import GoogleDriveService


class RemoteFilesTreeBuilder:

    def __init__(self, credetials_file):
        self.elements = {}
        self.google_drive_service = GoogleDriveService(ApplicationConstsEnum.GOOGLE_API_SCOPE, credetials_file)


    def __create_root_folder(self, root):
        pass

