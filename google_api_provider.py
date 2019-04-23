import requests

from enums.application_consts_enum import ApplicationConstsEnum
from services import auth_service


class GoogleApiProvider:

    def __init__(self, scope,  credentials_file, fields=["id", "name", "mimeType"]):
        self.fields = fields
        self.token = auth_service.auth(scope, credentials_file).getCredetials().token

    def find_all(self):
        return self.__create_get_request("https://www.googleapis.com/drive/v3/files").json()

    def find_files_for_folder_id(self, folder_id):
        res = self.__create_get_request("https://www.googleapis.com/drive/v3/files?q='{}'+in+parents".format(folder_id))
        if res.status_code == 200:
            return res.json()['files']
        return res.json()

    def find_file_by_id(self, file_id):
        return self.__create_get_request("https://www.googleapis.com/drive/v3/files/{}".format(file_id)).json()

    def __create_get_request(self, url):
        headers = {'Accept': 'application/json', 'Authorization': 'Bearer {}'.format(self.token)}
        fields = self.__create_fields_url_part(['id', 'name', 'md5Checksum', 'mimeType', 'parents'])
        res = requests.get(url+"?fields={}".format(fields), headers=headers)
        print(res.url)
        return res

    @staticmethod
    def __create_fields_url_part(fields):
        result = ''
        for f in fields:
            result = result + f + '%2C%20'
        return result[:-6]

gap = GoogleApiProvider(ApplicationConstsEnum.GOOGLE_API_SCOPE.value, ApplicationConstsEnum.CREDENTIALS_FILE.value)
response = gap.find_file_by_id('1WC7XWLgw1ipdM3qL9iyumX7p9bkHr9Ib')
print(response)
