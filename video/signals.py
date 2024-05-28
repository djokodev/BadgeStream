from django.db.models.signals import pre_save
from django.dispatch import receiver
from video.models import AnimatedVideo
from .helpers import format_size_verify

@receiver(pre_save, sender=AnimatedVideo)
def validate_video_format_and_size(sender, instance, **kwargs):
    if instance.file:
        format_size_verify(instance.file)