from services.drive_service import DriverSerivce
from services.local_tree_builder import LocalFilesTreeBuilder


class GoogleDriveSynch:

    FOLDER_MIMETYPE = 'application/vnd.google-apps.folder'
    GOOGLE_DOCUMENT_MIMETYPE = 'application/vnd.google-apps.document'
    CREDENTIALS_FILE = 'credentials.json'
    GOOGLE_FOLDER_MIMETYPE = 'application/vnd.google-apps.folder'

    def __init__(self, local_root_folder_path):
        self.drive_service = DriverSerivce(
            scopes='https://www.googleapis.com/auth/drive',
            credetials_file=GoogleDriveSynch.CREDENTIALS_FILE
        )
        self.local_root_folder_path = local_root_folder_path
        self.localTree = LocalFilesTreeBuilder(local_root_folder_path)


gds = GoogleDriveSynch('/home/sluski/Documents/Laptop/Documents/files')


#

def foo(id):
    for item in gds.drive_service.search_files_for_folder(id):
        if (item['mimeType'] == ''):
            foo(item['id'])
        else:
            print(item)


foo('root')
