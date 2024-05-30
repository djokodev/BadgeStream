from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from video.models import AnimatedVideo
from .models import Badge
from badges.helpers import check_views_and_assign_badge, check_veteran_status_and_assign_badge

@receiver(post_save, sender=AnimatedVideo)
def update_badge(sender, instance, created, **kwargs):
    if not created:
        check_views_and_assign_badge(instance)


@receiver(user_logged_in)
def check_veteran_status_on_login(sender, user, request, **kwargs):
    check_veteran_status_and_assign_badge(user)