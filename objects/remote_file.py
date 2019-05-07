from enums.application_consts_enum import ApplicationConstsEnum
from enums.file_type_enum import FileTypeEnum
from objects.file import File


class RemoteFile(File):
    def __init__(self, remote_id, name, type, created, md5=None, size=None):
        File.__init__(self, name, type, created, md5, size)
        self.remote_id = remote_id

    def __str__(self):
        result = [
            "Remote id: {}".format(self.remote_id),
            "Name: {} \n".format(self.name),
            "Type: {} \n".format(self.type),
            "MD5: {} \n".format(self.md5),
            "Size: {} \n".format(self.size),
            "Created: {} \n".format(self.created)
        ]
        return ''.join(result)

    def is_folder(self):
        return self.type == FileTypeEnum.FOLDER.value