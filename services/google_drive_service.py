from __future__ import print_function

import io

from googleapiclient.discovery import build, Resource
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

from enums.application_consts_enum import ApplicationConstsEnum
from enums.file_type_enum import FileTypeEnum
from google_api_provider import GoogleApiProvider
from objects.remote_file import RemoteFile
from services import auth_service


class GoogleDriveService:

    def __init__(self, scopes, credetials_file):
        self.drive_service = GoogleApiProvider(scopes, credetials_file)

    def find_files_by_folder_id(self, parent_id):
        res = self.drive_service.find_files_for_folder_id(parent_id)
        print("res", res)
        # return RemoteFile(
        #     remote_id=res["id"],
        #     name=res["name"],
        #     type=self.__mime_type_to_enum_type(res["mimeType"]),
        #     created=res["createdTime"]
        # )

    def find_file_by_id(self, file_id):
        json_response = self.drive_service.find_file_by_id(file_id)
        return RemoteFile(
            remote_id=json_response["id"],
            name=json_response["name"],
            type=self.__mime_type_to_enum_type(json_response["mimeType"]),
            created=json_response["createdTime"]
        )

    @staticmethod
    def __mime_type_to_enum_type(mime_type):
        if mime_type == ApplicationConstsEnum.FOLDER_MIMETYPE.value:
            return FileTypeEnum.FOLDER.value
        else:
            return FileTypeEnum.FILE.value
