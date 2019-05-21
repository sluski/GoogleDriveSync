import os

from enums.file_type_enum import FileTypeEnum
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

        folder_sorted = False
        folders = []
        files = []
        for k, v in self.remoteTree.elements.items():
            if v.thing.type == FileTypeEnum.FOLDER.value:
                folders.append(k)
            else:
                files.append((k))

        while not folder_sorted:
            folder_sorted = True
            for i in range(folders.__len__() - 1):
                j = i + 1
                if folders[i].split("/").__len__() > folders[j].split("/").__len__():
                    temp = folders[i]
                    folders[i] = folders[j]
                    folders[j] = temp
                    folder_sorted = False
            print(folders)

        files_sorted = False
        while not files_sorted:
            files_sorted = True
            for i in range(files.__len__() - 1):
                j = i + 1
                if files[i].split("/").__len__() > files[j].split("/").__len__():
                    temp = files[i]
                    files[i] = files[j]
                    files[j] = temp
                    files_sorted = False
            print(files)




        for k, v in local_to_remote.items():
            # root_path = ""
            # for n in (local_root_folder_path + k[1:]).split("/")[1:-1]
            #     root_path += "/" + n
            if v.thing.type == FileTypeEnum.FOLDER.value:
                print("Creating directory {}".format(v.thing.name))
                path = local_root_folder_path + k[1:]
                os.mkdir(path)

        for k, v in local_to_remote.items():
            if v.thing.type == FileTypeEnum.FILE.value:
                print("Downloading {} with id: {}".format(v.thing.name, v.thing.remote_id))
                path = local_root_folder_path + k[1:] + "." + v.thing.mimeType.split("/")[1]
                self.remoteTree.google_drive_service.download_file(v.thing.remote_id, path)


gds = GoogleDriveSynch('/home/sluski/Documents/files2')
