from services.google_drive_service import GoogleDriveService
from services.local_tree_builder import LocalFilesTreeBuilder
from services.remote_tree_builder import RemoteFilesTreeBuilder


class GoogleDriveSynch:

    def __init__(self, local_root_folder_path):
        self.local_root_folder_path = local_root_folder_path
        self.localTree = LocalFilesTreeBuilder(local_root_folder_path)
        self.remoteTree = RemoteFilesTreeBuilder('root')


        '''
        local_to_remote - files that are on local but are not on remote
        modified - files that are locally and remotely  but md5 hashes are diferrent
        remote_to_local - files that are on remote but are not on local
        '''
        remote_to_local, local_to_remote = {}, {}
        modified = {}

        for k, v in self.remoteTree.elements.items():
            if not self.localTree.elements.__contains__(k):
                local_to_remote[k] = v
            elif self.remoteTree.elements.get(k).thing.md5 != self.localTree.elements.get(k).thing.md5:
                modified[k] = v

        for k, v in self.localTree.elements.items():
            if not self.remoteTree.elements.__contains__(k):
                remote_to_local[k] = v
            elif self.remoteTree.elements.get(k).thing.md5 != self.localTree.elements.get(k).thing.md5:
                modified[k] = v

        for k, v in local_to_remote.items():
            print("Downloading {} with id: {}".format(v.thing.name, v.thing.remote_id))
            path = local_root_folder_path + k[1:] + "." +  v.thing.mimeType.split("/")[1]
            print(k, v)
            print(path)
            self.remoteTree.google_drive_service.download_file(v.thing.remote_id, path)



gds = GoogleDriveSynch('/home/sluski/Documents/files')
