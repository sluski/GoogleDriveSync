import hashlib
import os


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
        return path.split("/")[-1]

    @staticmethod
    def get_parent_path(path, sep=os.sep):
        splitted = path.split(sep)
        concatenate_paths = lambda a, b: a + sep + b
        result = ''
        del splitted[-1]
        for ele in splitted:
            result = concatenate_paths(result, ele) if ele is not '' else result
        return result
