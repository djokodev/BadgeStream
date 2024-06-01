from .models import Badge
from video.models import AnimatedVideo
from django.utils import timezone
from datetime import timedelta

def assign_star_rising_badge(user):
    badge, created = Badge.objects.get_or_create(
        name="Étoile Montante",
        defaults={
            "description": "Attribuer pour avoir atteind 1000 vues sur une de vos videos",  
        },
    )
    
    if not user.badges.filter(id=badge.id).exists():
        user.badges.add(badge)
        user.save()

def check_views_and_assign_badge(video):
    print(video.views)
    video.refresh_from_db()
    print(video.views)
    if video.views >= 1000:
        assign_star_rising_badge(video.uploaded_by)

def assign_veteran_badge(user):
    badge, created = Badge.objects.get_or_create(
        name="Vétéran",
        defaults={
            "description": "Un utilisateur est inscrit sur le site depuis un an déjà",
        },
    )
    if not user.badges.filter(id=badge.id).exists():
        user.badges.add(badge)
        user.save()

def check_veteran_status_and_assign_badge(user):
    one_year_ago = timezone.now() - timedelta(days=365)
    if user.date_joined <= one_year_ago:
        assign_veteran_badge(user)


def assign_collector_badge(user):
    badge, created = Badge.objects.get_or_create(
        name="Collectionneur",
        defaults={
            "description": "Attribué pour avoir téléverser plus de 5 vidéos",
        },
    )
    
    if not user.badges.filter(id=badge.id).exists():
        user.badges.add(badge)
        user.save()

def check_collector_status_and_assign_badge(user):
    uploaded_videos_count = AnimatedVideo.objects.filter(uploaded_by=user).count()
    if uploaded_videos_count >= 5:
        assign_collector_badge(user)


def remove_collector_badge(user):
    try:
        collector_badge = Badge.objects.get(name="Collectionneur")
        user.badges.remove(collector_badge)
        user.save()
    except Badge.DoesNotExist:
        pass
