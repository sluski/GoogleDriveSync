import hashlib


class Common:

    @staticmethod
    def generate_md5(file):
        hash_md5 = hashlib.md5()
        with open(file, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    @staticmethod
    def extract_name_from_path(path):
        return path.split("/")[-2]