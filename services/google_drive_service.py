from __future__ import print_function

import io

from googleapiclient.discovery import build, Resource
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

from google_api_provider import GoogleApiProvider
from services import auth_service


class GoogleDriveService:
    FOLDER_MIMETYPE = 'application/vnd.google-apps.folder'
    GOOGLE_DOCUMENT_MIMETYPE = 'application/vnd.google-apps.document'
    DEFAULT_FILES = ['id', 'name', 'md5Checksum', 'mimeType', 'exportLinks']

    def __init__(self, scopes, credetials_file):
        self.drive_service = GoogleApiProvider(scopes, credetials_file)

    # def list_files(self, size):
    #     results = self.drive_service.files().list(
    #         pageSize=size, fields="nextPageToken, {}".format(GoogleDriveService.DEFAULT_FILES)).execute()
    #     return results.get('files', [])
    #
    # def list_files_only(self, size=100):
    #     result = []
    #     for item in self.list_files(size):
    #         if item['mimeType'] not in [GoogleDriveService.FOLDER_MIMETYPE, GoogleDriveService.GOOGLE_DOCUMENT_MIMETYPE]:
    #             result.append(item)
    #     return result
    #
    # def save_file(self, filename, filepath, mimetype):
    #     file_metadata = {'name': filename}
    #     media = MediaFileUpload(filename=filepath,
    #                             mimetype=mimetype)
    #     return self.drive_service.files().create(body=file_metadata,
    #                                              media_body=media,
    #                                              fields='id').execute()
    #
    # def download_file(self, file_id, file_path):
    #     request = self.drive_service.files().get_media(fileId=file_id)
    #     bio = io.BytesIO()
    #     downloader = MediaIoBaseDownload(bio, request)
    #     done = False
    #     while done is False:
    #         status, done = downloader.next_chunk()
    #         print("Download %d%%." % int(status.progress() * 100))
    #     with open(file_path, 'wb') as f:
    #         bio.seek(0)
    #         f.write(bio.read())

    # def search_file(self, size, query):
    #     results = self.drive_service.files().list(
    #         pageSize=size, fields="nextPageToken, %s" % GoogleDriveService.DEFAULT_FILES, q=query).execute()
    #     print(results)
    #     items = results.get('files', [])
    #
    #     return items

    # def search_file_that_contains(self, size, name):
    #     query = "name contains '{}'".format(name)
    #     return self.search_file(self, size, query)
    #
    # def search_files_by_mediatype(self, size, mimetype):
    #     query = "mimeType = '{}'".format(mimetype)
    #     return self.search_file(self, size, query)
    #
    # def search_files_for_folder(self, folder_id):
    #     query = "'{}' in parents".format(folder_id)
    #     return self.search_file(100, query)

    def search_file_by_id(self, file_id):
        # return self.drive_service.find_file(file_id, fields=self.DEFAULT_FILES)
        return self.drive_service.find_files_for_folder_id('1fA0ETdehB-M2YUx3JZp49Z_OI7oroh8t')
        # self.drive_service.list_all('1fA0ETdehB-M2YUx3JZp49Z_OI7oroh8t')