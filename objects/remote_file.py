from objects.file import File


class RemoteFile(File):
    def __init__(self, remote_id, name, type, created, md5=None, size=None):
        File.__init__(self, name, type, created, md5, size)
        self.remote_id = remote_id

    def __str__(self):
        return str(self.remote_id) + ", " + str(self.name) + ", " + str(self.type) + ", " + str(self.created) + ", " + str(self.md5) + ", " + str(self.size)
