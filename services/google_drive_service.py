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
        result = []
        response_list = self.drive_service.find_files_for_folder_id(parent_id)
        for e in response_list:
            result.append(self.__create_new_element(e))

        return result

    def __create_new_element(self, res):
        if self.__mime_type_to_enum_type(res["mimeType"]) == FileTypeEnum.FILE.value:
            return self.__create_new_file(res)
        else:
            return self.__create_new_folder(res)

    def __create_new_folder(self, res):
        return RemoteFile(
                remote_id=res["id"],
                name=res["name"],
                type=self.__mime_type_to_enum_type(res["mimeType"]),
                created=res["createdTime"]
            )

    def __create_new_file(self, res):
        return RemoteFile(
            remote_id=res["id"],
            name=res["name"],
            type=self.__mime_type_to_enum_type(res["mimeType"]),
            created=res["createdTime"],
            md5=res["md5Checksum"],
            size="size"
        )

    def find_file_by_id(self, file_id):
        json_response = self.drive_service.find_file_by_id(file_id)
        return self.__create_new_element(json_response)

    @staticmethod
    def __is_folder(mime_type):
        return  mime_type == ApplicationConstsEnum.FOLDER_MIMETYPE.value

    @staticmethod
    def __mime_type_to_enum_type(mime_type):
        if mime_type == ApplicationConstsEnum.FOLDER_MIMETYPE.value:
            return FileTypeEnum.FOLDER.value
        else:
            return FileTypeEnum.FILE.value
