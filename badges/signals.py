from django.db.models.signals import post_save
from django.dispatch import receiver
from video.models import AnimatedVideo
from .models import Badge
from badges.helpers import check_views_and_assign_badge

@receiver(post_save, sender=AnimatedVideo)
def update_badge(sender, instance, created, **kwargs):
    if not created:
        check_views_and_assign_badge(instance)
