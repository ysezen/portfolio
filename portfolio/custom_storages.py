from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

if settings.DEBUG:
    from django.core.files.storage import FileSystemStorage

    class StaticStorage(FileSystemStorage):
        file_overwrite = False
        default_acl = 'public-read'


    class MediaStorage(FileSystemStorage):
        file_overwrite = False
        default_acl = 'public-read'


    class DocumentStorage(FileSystemStorage):
        file_overwrite = False
        default_acl = 'public-read'


    class ImageSettingStorage(FileSystemStorage):
        file_overwrite = False
        default_acl = 'public-read'
else:

    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION
        querystring_auth = False


    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION
        file_overwrite = False


    class DocumentStorage(S3Boto3Storage):
        location = settings.DOCUMENTS_LOCATION
        file_overwrite = False


    class ImageSettingStorage(S3Boto3Storage):
        location = settings.IMAGE_SETTINGS_LOCATION
        file_overwrite = False
