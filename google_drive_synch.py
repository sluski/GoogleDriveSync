import hashlib, os, os.path

from drive_service import DriverSerivce
from common import Map, Pair, File


class GoogleDriveSynch:
    FOLDER_MIMETYPE = 'application/vnd.google-apps.folder'
    GOOGLE_DOCUMENT_MIMETYPE = 'application/vnd.google-apps.document'

    def __init__(self, folder_path):
        self.matched_files = []
        self.drive_service = DriverSerivce(
            'https://www.googleapis.com/auth/drive',
            'credentials.json')
        self.folder_path = folder_path
        self.__take_metadata_from_local()
        self.__take_metadata_from_remote()

    def synchronize(self):
        pass

    '''
        Download all files (not folders) from google drive to defined folder. In case if this same file (comparing md5)
        is actually on local disc it will ignore downloading file
    '''
    def download_all(self):
        for file in self.matched_files:
            remote_obj = file.get('r_object')
            new_file_path = self.folder_path + remote_obj['name']
            if os.path.isfile(new_file_path) and self.__generate_md5(new_file_path) != remote_obj['md5Checksum']:
                os.remove(new_file_path)
                self.__create_new_file(new_file_path)
                self.drive_service.download_file(remote_obj['id'], new_file_path)
            else:
                self.drive_service.download_file(remote_obj['id'], new_file_path)

    '''
        Adds local files metadata to class variable which contains data about local and remote files 
    '''
    def __take_metadata_from_local(self):
        for file in self.__find_files_for_path(self.folder_path):
            self.matched_files.append(
                Map(file, Pair(File(file, self.__generate_md5(self.__create_file_path(file))), None)))


    '''
        Adds remote files metadata to class variable which contains data about local and remote files
    '''
    def __take_metadata_from_remote(self):
        for item in self.drive_service.list_files_only():
            for map in self.matched_files:
                if map.key == item['name']:
                    map.value.second = File(item['name'], item['md5Checksum'],
                                            {'mimeType': item['mimeType'], 'id': item['id']})
                    break

    '''
        Returns list of files (not folders) for defined path
    '''
    @staticmethod
    def __find_files_for_path(path):
        return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]


    '''
        Creates new file if not exist
    '''
    @staticmethod
    def __create_new_file(new_file_path):
        a = open(new_file_path, "w+")
        a.close()

    '''
        Concatenate folder_path to file_name
    '''
    def __create_file_path(self, fname):
        return self.folder_path + fname

    '''
        Generate md5 based on file
    '''
    @staticmethod
    def __generate_md5(file):
        hash_md5 = hashlib.md5()
        with open(file, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()


googleDrive = GoogleDriveSynch("/home/sluski/files/")
for i in googleDrive.matched_files:
    print(i.value.first.return_as_dict())
    print(i.value.second.return_as_dict())
# googleDrive.synchronize()
# googleDrive.download_all()
# print(googleDrive.matched_files)
