from services.local_tree_builder import LocalFilesTreeBuilder
from services.remote_tree_builder import RemoteFilesTreeBuilder


class GoogleDriveSynch:

    def __init__(self, local_root_folder_path):
        self.local_root_folder_path = local_root_folder_path
        self.localTree = LocalFilesTreeBuilder(local_root_folder_path)
        self.remoteTree = RemoteFilesTreeBuilder('root')

        remote_to_local, remote_to_local_override = [], []
        local_to_remote, local_to_remote_override = [], []

        for k, v in self.remoteTree.elements.items():
            print(k)
            if not self.localTree.elements.__contains__(k):
                local_to_remote.append({k, v})
            elif self.remoteTree.elements.get(k).thing.md5 != self.localTree.elements.get(k).thing.md5:
                local_to_remote_override.append({k, v})

        print("_______")

        for k, v in self.localTree.elements.items():
            print(k)
            if not self.remoteTree.elements.__contains__(k):
                remote_to_local.append({k, v})
            elif self.remoteTree.elements.get(k).thing.md5 != self.localTree.elements.get(k).thing.md5:
                remote_to_local_override.append({k, v})

        print(local_to_remote)
        print(local_to_remote_override)
        print(remote_to_local)
        print(remote_to_local_override)


gds = GoogleDriveSynch('/home/sluski/Documents/files')
