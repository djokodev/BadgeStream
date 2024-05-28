import magic
from django.conf import settings
from django.core.exceptions import ValidationError

def format_size_verify(file):
    mime = magic.Magic(mime=True)
    file_mime_type = mime.from_buffer(file.read(1024))
    file.seek(0) 

    allowed_mime_types = {
        'mp4': 'video/mp4',
        'avi': 'video/x-msvideo',
        'mov': 'video/quicktime'
    }

    file_extension = file.name.split('.')[-1].lower()
    if file_extension not in settings.ALLOWED_VIDEO_FORMATS:
        raise ValidationError(f"Format non supporté: {file_extension}. Les formats supportés sont {settings.ALLOWED_VIDEO_FORMATS}")

    if file_mime_type != allowed_mime_types[file_extension]:
        raise ValidationError(f"Type MIME non supporté: {file_mime_type}. Le type MIME doit être {allowed_mime_types[file_extension]}")

    file_size_mb = file.size / (1024 * 1024)
    if file_size_mb > settings.MAX_VIDEO_SIZE_MB:
        raise ValidationError(f"La taille du fichier {file_size_mb:.2f} MB dépasse la taille maximale autorisée de {settings.MAX_VIDEO_SIZE_MB} MB")
