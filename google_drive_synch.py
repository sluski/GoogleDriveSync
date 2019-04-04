from enums.application_consts_enum import ApplicationConstsEnum
from services.drive_service import DriverSerivce
from services.local_tree_builder import LocalFilesTreeBuilder


class GoogleDriveSynch:

    def __init__(self, local_root_folder_path):
        self.drive_service = DriverSerivce(
            scopes='https://www.googleapis.com/auth/drive',
            credetials_file=ApplicationConstsEnum.CREDENTIALS_FILE
        )
        self.local_root_folder_path = local_root_folder_path
        self.localTree = LocalFilesTreeBuilder(local_root_folder_path)


gds = GoogleDriveSynch('/home/sluski/Documents/Laptop/Documents/files')

