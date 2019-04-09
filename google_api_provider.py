import requests
from services import auth_service


class GoogleApiProvider:

    DEFAULT_FIELDS = ["id", "name", "mimeType"]

    def __init__(self, scope, credentials_file):
        auth_instance = auth_service.auth(scope, credentials_file)
        self.credentials = auth_instance.getCredetials()
        self.token = self.credentials.token

    def find_files_for_folder_id(self, folder_id='root', fields=["id", "name", "mimeType"]):
        response = self.__create_request("https://www.googleapis.com/drive/v3/files?q=%27{}%27%20in%20parents&fields={}".format(folder_id, self.__generate_url_part_for_fields(fields, '%20')))
        if response.status_code == 200:
            return response.json()['files']
        return response.json()

    def find_file(self, file_id, fields=DEFAULT_FIELDS):
        response = self.__create_request('https://www.googleapis.com/drive/v3/files/{}?fields={}'.format(file_id, self.__generate_url_part_for_fields(fields, '%2C%20')))
        return response.json()

    def __create_request(self, url):
        headers = {'Accept': 'application/json', 'Authorization': 'Bearer {}'.format(self.token)}
        res = requests.get(url, headers=headers)
        return res


    @staticmethod
    def __generate_url_part_for_fields(fields_tab, separator):
        """
        Generates part of url that will be pass to ?fields
        example: __generate_url_part_for_fields(['id', 'md5Checksum', 'mimeType']) returns id%2C%20md5Checksum%2C%20mimeType
        :param fields_tab: [] of fileds ex. ['id', 'md5Checksum', 'mimeType']
        :return:
        """

        result = ""
        for t in fields_tab:
            result += t + separator
        sep_len = len(separator)
        return result[:sep_len]  # removes last '%2C%20' from string
