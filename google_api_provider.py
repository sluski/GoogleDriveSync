import requests

from enums.application_consts_enum import ApplicationConstsEnum
from services import auth_service


class GoogleApiProvider:

    def __init__(self, scope,  credentials_file, fields=["id", "name", "mimeType", "createdTime", "md5Checksum", "size"]):
        self.fields = fields
        self.__concatenated_fields = self.__create_fields_url_part(self.fields)
        self.token = auth_service.auth(scope, credentials_file).getCredetials().token

    def find_files_for_folder_id(self, folder_id):
        query = self.__format_to_utf_8("'{}' in parents".format(folder_id))
        res = self.__create_get_request("https://www.googleapis.com/drive/v3/files?q={}".format(query))
        if res.status_code == 200:
            return res.json()['files']

        return res.json()

    def find_file_by_id(self, file_id):
        return self.__create_get_request("https://www.googleapis.com/drive/v3/files/{}".format(file_id)).json()

    def __create_get_request(self, url, defined_fields=True):
        headers = {'Accept': 'application/json', 'Authorization': 'Bearer {}'.format(self.token)}
        if defined_fields:
            res = requests.get(url + "?fields={}".format(self.__concatenated_fields), headers=headers)
        else:
            res = requests.get(url, headers=headers)

        print(res.url)
        return res

    @staticmethod
    def __create_fields_url_part(fields):
        result = ''
        for f in fields:
            result = result + f + ApplicationConstsEnum.GOOGLE_URL_SEPARATOR.value
        return result[:-6]

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



