from enums.application_consts_enum import ApplicationConstsEnum
from services.google_drive_service import GoogleDriveService
from services.local_tree_builder import LocalFilesTreeBuilder
from services.remote_tree_builder import RemoteFilesTreeBuilder


class GoogleDriveSynch:

    def __init__(self, local_root_folder_path):
        self.local_root_folder_path = local_root_folder_path
        self.localTree = LocalFilesTreeBuilder(local_root_folder_path)
        self.remoteTree = RemoteFilesTreeBuilder('root')

gds = GoogleDriveSynch('/home/sluski/Documents/Laptop/Documents/files')
