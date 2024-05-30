from .models import Badge
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
    if video.views >= 1000:
        assign_star_rising_badge(video.uploaded_by)


def assign_veteran_badge(user):
    badge, created = Badge.objects.get_or_create(
        name="Vétéran",
        defaults={
            "description": "Un utilisateur est inscrit sur le site depuis un an déjà",
        },
    )
    
    if created: 
        user.badges.add(badge)
        user.save()

def check_veteran_status_and_assign_badge(user):
    one_year_ago = timezone.now() - timedelta(days=365)
    if user.date_joined <= one_year_ago:
        assign_veteran_badge(user)