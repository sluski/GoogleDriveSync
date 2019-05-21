from enums.application_consts_enum import ApplicationConstsEnum
from enums.file_type_enum import FileTypeEnum
from objects.file import File


class RemoteFile(File):
    def __init__(self, remote_id, name, type, created, mimeType=None, md5=None, size=None):
        File.__init__(self, name, type, created, md5, size)
        self.remote_id = remote_id
        self.mimeType = mimeType

    def __str__(self):
        result = [
            "Remote id: {} \n".format(self.remote_id),
            "Name: {} \n".format(self.name),
            "MD5: {} \n".format(self.md5),
            "Type: {} \n".format(self.type),
            "MimeType: {}".format(self.mimeType)
        ]
        return ''.join(result)

    def is_folder(self):
        return self.type == FileTypeEnum.FOLDER.value