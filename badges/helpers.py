from .models import Badge

def assign_star_rising_badge(user):
    badge, created = Badge.objects.get_or_create(
        name="Étoile Montante",
        defaults={
            "image": "img/badge1.jpg",  
            "description": "Attribuer pour avoir atteind 1000 vues sur une video",  
        },
    )
    
    if not user.badges.filter(id=badge.id).exists():
        user.badges.add(badge)
        user.save()


def check_views_and_assign_badge(video):
    if video.views >= 1000:
        assign_star_rising_badge(video.uploaded_by)
