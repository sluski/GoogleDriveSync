import requests
from services import auth_service


class GoogleApiProvider:

    def __init__(self, scope,  credentials_file, fields=["id", "name", "mimeType"]):
        self.fields = fields
        self.token = auth_service.auth(scope, credentials_file).getCredetials().token

    def find_all(self):
        return self.__create_get_request("https://www.googleapis.com/drive/v3/files").json()

    def find_files_for_folder_id(self, folder_id):
        response = self.__create_get_request("https://www.googleapis.com/drive/v3/files?q='{}'+in+parents".format(folder_id))
        if response.status_code == 200:
            return response.json()['files']
        return response.json()

    def __create_get_request(self, url):
        headers = {'Accept': 'application/json', 'Authorization': 'Bearer {}'.format(self.token)}
        res = requests.get(url, headers=headers)
        return res
