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
        self.tree = FilesTreeBuilder(folder_path)
        self.__create_local_tree(folder_path)

    def __create_local_tree(self, path):
        for entry in os.scandir(path):
            if os.path.isdir(entry.path):
                self.tree.add_folder(entry.path, self.tree.find_element_for_path(self.__generate_parent_path(entry.path)))
                self.__create_local_tree(entry.path)
            elif os.path.isfile(entry.path):
                self.tree.add_file(entry.path, self.tree.find_element_for_path(self.__generate_parent_path(entry.path)))

    @staticmethod
    def __generate_parent_path(path):
        splitted = path.split(os.sep)
        concatenate_paths = lambda a, b: a + os.sep + b
        result = ''
        del splitted[-1]
        for ele in splitted:
            result = concatenate_paths(result, ele) if ele is not '' else result
        return result

    @staticmethod
    def __generate_md5(file):
        hash_md5 = hashlib.md5()
        with open(file, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()


gds = GoogleDriveSynch('/home/sluski/Documents/Laptop/Documents/files')
print(gds.root)
