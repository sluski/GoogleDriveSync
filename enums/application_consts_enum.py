from enum import Enum
import os


class ApplicationConstsEnum(Enum):
    FOLDER_MIMETYPE = 'application/vnd.google-apps.folder'
    GOOGLE_DOCUMENT_MIMETYPE = 'application/vnd.google-apps.document'
    CREDENTIALS_FILE = ".." + os.sep + "assets" + os.sep + 'credentials.json'
    GOOGLE_FOLDER_MIMETYPE = 'application/vnd.google-apps.folder'
    GOOGLE_API_SCOPE = 'https://www.googleapis.com/auth/drive'
    GOOGLE_URL_SEPARATOR = '%2C%20'
