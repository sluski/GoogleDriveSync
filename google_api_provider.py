import requests

from enums.application_consts_enum import ApplicationConstsEnum
from services import auth_service


class GoogleApiProvider:

    def __init__(self, scope,  credentials_file, fields=["id", "name", "mimeType", "createdTime", "md5Checksum", "size"]):
        self.fields = fields
        self.__concatenated_fields = self.__concatenate_fields(fields)
        self.token = auth_service.auth(scope, credentials_file).getCredetials().token

    def find_files_for_folder_id(self, folder_id):
        res = self.__create_get_files_request(folder_id)
        if res.status_code == 200:
            return res.json()['files']
        return res.json()

    def find_file_by_id(self, file_id):
        return self.__create_get_file_request(file_id).json()

    def __create_get_file_request(self, file_id):
        url = "https://www.googleapis.com/drive/v3/files/{}".format(file_id)
        headers = {'Accept': 'application/json', 'Authorization': "Bearer {}".format(self.token)}
        req = requests.get(url + "?fields={}".format(self.__concatenated_fields), headers=headers)
        return req

    def __create_get_files_request(self, parent_id):
        headers = {'Accept': 'application/json', 'Authorization': 'Bearer {}'.format(self.token)}
        res = requests.get("https://www.googleapis.com/drive/v3/files?q='{}' in parents&fields=files({})".format(parent_id, self.__concatenated_fields), headers=headers)
        return res

    @staticmethod
    def __concatenate_fields(fields):
        result = ""
        for f in fields:
            result = result + f + ", "
        return result[:-2]

    @staticmethod
    def __format_to_utf_8(unformatted_string):
        result = ""
        utf_8_chars = {"'": "%27", " ": "%20", ",": "%2C", "!": "%21", "\"": "%22", "&": "%26", "%": "%25"}
        for i in range(unformatted_string.__len__()):
            if utf_8_chars.__contains__(unformatted_string[i]):
                result = result + utf_8_chars[unformatted_string[i]]
            else:
                result = result + unformatted_string[i]
        return result


# gap = GoogleApiProvider(ApplicationConstsEnum.GOOGLE_API_SCOPE.value, ApplicationConstsEnum.CREDENTIALS_FILE.value)
#
# print(gap.find_files_for_folder_id('root'))
# print(gap.find_file_by_id('1WC7XWLgw1ipdM3qL9iyumX7p9bkHr9Ib'))
