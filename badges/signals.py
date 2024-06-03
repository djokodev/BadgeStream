from django.db.models.signals import post_save, post_delete
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from video.models import AnimatedVideo
from .models import Badge
from badges.helpers import check_views_and_assign_star_rising_badge, check_veteran_status_and_assign_badge, check_collector_status_and_assign_badge, remove_collector_badge

@receiver(post_save, sender=AnimatedVideo)
def assign_star_rising_or_collector_badge(sender, instance, created, update_fields=None, **kwargs): # TODO: modifier le nom
    if update_fields and 'views' in update_fields:
        check_views_and_assign_star_rising_badge(instance)
    elif created:
        check_collector_status_and_assign_badge(instance.uploaded_by)


@receiver(user_logged_in)
def assign_veteran_status(sender, user, request, **kwargs):
    check_veteran_status_and_assign_badge(user)


@receiver(post_delete, sender=AnimatedVideo)
def remove_collector_badge_from_user(sender, instance, **kwargs):
    user = instance.uploaded_by
    uploaded_videos_count = AnimatedVideo.objects.filter(uploaded_by=user).count()
    
    if uploaded_videos_count < 5:
        remove_collector_badge(user)


