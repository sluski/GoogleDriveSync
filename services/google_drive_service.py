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

    def files_by_id(self, parent_id):
        print(self.drive_service.find_files_for_folder_id(parent_id))
