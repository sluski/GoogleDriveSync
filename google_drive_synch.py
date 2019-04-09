from enums.application_consts_enum import ApplicationConstsEnum
from services.google_drive_service import GoogleDriveService
from services.local_tree_builder import LocalFilesTreeBuilder
from services.remote_tree_builder import RemoteFilesTreeBuilder


class GoogleDriveSynch:

    def __init__(self, local_root_folder_path):
        self.local_root_folder_path = local_root_folder_path
        self.localTree = LocalFilesTreeBuilder(local_root_folder_path)
        self.remoteTree = RemoteFilesTreeBuilder()


# gds = GoogleDriveSynch('/home/sluski/Documents/Laptop/Documents/files')

gds = GoogleDriveService(ApplicationConstsEnum.GOOGLE_API_SCOPE, ApplicationConstsEnum.CREDENTIALS_FILE)

#
# def foo(id):
#     for item in gds.search_files_for_folder(id):
#         if (item['mimeType'] == ''):
#             print(item)
#             foo(item['id'])
#         else:
#             print(item)


# for v in gds.search_file_by_id("1r_TE3MkUMw5yxM9QEKGwM6L1VeBQVRXH"):
#     print(v)
# exportLinks 1fA0ETdehB-M2YUx3JZp49Z_OI7oroh8t
print(gds.search_file_by_id('1r_TE3MkUMw5yxM9QEKGwM6L1VeBQVRXH'))
