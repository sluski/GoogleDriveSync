from __future__ import print_function

import io

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

from services import auth_service


class DriverSerivce:
    FOLDER_MIMETYPE = 'application/vnd.google-apps.folder'
    GOOGLE_DOCUMENT_MIMETYPE = 'application/vnd.google-apps.document'
    DEFAULT_FILES = 'files(id, name, md5Checksum, mimeType)'

    def __init__(self, scopes, credetials_file):
        self.auth_instance = auth_service.auth(scopes, credetials_file)
        self.creds = self.auth_instance.getCredetials()
        self.drive_service = build('drive', 'v3', credentials=self.creds)

    def list_files(self, size):
        results = self.drive_service.files().list(
            pageSize=size, fields="nextPageToken, {}".format(DriverSerivce.DEFAULT_FILES)).execute()
        return results.get('files', [])

    def list_files_only(self, size=100):
        result = []
        for item in self.list_files(size):
            if item['mimeType'] not in [DriverSerivce.FOLDER_MIMETYPE, DriverSerivce.GOOGLE_DOCUMENT_MIMETYPE]:
                result.append(item)
        return result

    def save_file(self, filename, filepath, mimetype):
        file_metadata = {'name': filename}
        media = MediaFileUpload(filename=filepath,
                                mimetype=mimetype)
        return self.drive_service.files().create(body=file_metadata,
                                                 media_body=media,
                                                 fields='id').execute()

    def download_file(self, file_id, file_path):
        request = self.drive_service.files().get_media(fileId=file_id)
        bio = io.BytesIO()
        downloader = MediaIoBaseDownload(bio, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("Download %d%%." % int(status.progress() * 100))
        with open(file_path, 'wb') as f:
            bio.seek(0)
            f.write(bio.read())

    def __search_file(self, size, query):
        results = self.drive_service.files().list(
            pageSize=size, fields="nextPageToken, %s" % DriverSerivce.DEFAULT_FILES, q=query).execute()
        print(results)
        items = results.get('files', [])

        return items

    def search_file_contains(self, size, name):
        query = "name contains '{}'".format(name)
        return self.search_file(self, size, query)

    def search_file_mediatype(self, size, mimetype):
        query = "mimeType = '{}'".format(mimetype)
        return self.search_file(self, size, query)

    def search_files_for_folder(self, folder_id):
        query = "'{}' in parents".format(folder_id)
        return self.__search_file(100, query)
