import hashlib
import os
import os.path

from services.drive_service import DriverSerivce
from services.tree_builder import FilesTreeBuilder


class GoogleDriveSynch:
    FOLDER_MIMETYPE = 'application/vnd.google-apps.folder'
    GOOGLE_DOCUMENT_MIMETYPE = 'application/vnd.google-apps.document'
    CREDENTIALS_FILE = 'credentials.json'

    def __init__(self, folder_path):
        self.drive_service = DriverSerivce(
            'https://www.googleapis.com/auth/drive',
            GoogleDriveSynch.CREDENTIALS_FILE)
        self.folder_path = folder_path
        self.localTree = FilesTreeBuilder(folder_path)
        self.__create_local_tree(folder_path)

    def __create_local_tree(self, path):
        for entry in os.scandir(path):
            if os.path.isdir(entry.path):
                self.localTree.add_folder(entry.path)
                self.__create_local_tree(entry.path)
            elif os.path.isfile(entry.path):
                self.localTree.add_file(entry.path)

    def __create_remote_tree(self):
        pass

gds = GoogleDriveSynch('/home/sluski/Documents/Laptop/Documents/files')
# for item in gds.drive_service.list_files(100):
print(gds.drive_service.search_files_for_folder('1fA0ETdehB-M2YUx3JZp49Z_OI7oroh8t'))

# print(gds.root)


