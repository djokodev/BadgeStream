from django.test import TestCase
from .models import Badge
from video.models import AnimatedVideo
from AuthUserManager.models import CustomeUser
from django.utils import timezone
from datetime import timedelta
from .helpers import ( 
    check_views_and_assign_badge, 
    check_veteran_status_and_assign_badge, 
    check_collector_status_and_assign_badge, 
    remove_collector_badge
)

class TestCaseBadge(TestCase):
    def setUp(self):
        self.badge = Badge.objects.create(name = "badge1", description = "description du badge1")
    
    def test_badge_creation(self):
        self.assertEqual(self.badge.name, "badge1")
        self.assertEqual(self.badge.description, "description du badge1")


class TestCaseAssignmentBage(TestCase):
    def setUp(self):   
        self.user = CustomeUser.objects.create(username='testuser', email='test@example.com', password='password')
        self.video = AnimatedVideo.objects.create(title='Test Video', uploaded_by=self.user)
        self.user.date_joined = timezone.now() - timedelta(days=365)
        self.user.save()

    def test_assign_star_rising_badge_less_than_1000_views(self):
        self.assertEqual(self.user.badges.count(), 0)
        self.video.views = 500
        self.video.save()
        check_views_and_assign_badge(self.video)
        self.assertEqual(self.user.badges.count(), 0)

    
    def test_assign_star_rising_badge_1000_views(self):
        self.assertEqual(self.user.badges.count(), 0)
        self.video.views = 1000
        self.video.save()
        check_views_and_assign_badge(self.video)
        self.assertEqual(self.user.badges.count(), 1)

    
    def test_check_veteran_status_and_assign_badge_less_than_one_year(self):
        self.user.date_joined = timezone.now() - timedelta(days=364)
        self.user.save()
        self.assertEqual(self.user.badges.count(), 0)
        check_veteran_status_and_assign_badge(self.user)
        self.assertEqual(self.user.badges.count(), 0)


    def test_check_veteran_status_and_assign_badge_more_than_one_year(self):
        self.user.date_joined = timezone.now() - timedelta(days=366)
        self.user.save()
        self.assertEqual(self.user.badges.count(), 0)
        check_veteran_status_and_assign_badge(self.user)
        self.assertEqual(self.user.badges.count(), 1)


    def test_check_collector_status_and_assign_badge_less_than_five_videos(self):
        for i in range(2):
            AnimatedVideo.objects.create(title=f'Test Video {i}', uploaded_by=self.user)
        self.assertEqual(self.user.badges.count(), 0)
        check_collector_status_and_assign_badge(self.user)
        self.assertEqual(self.user.badges.count(), 0)


    def test_check_collector_status_and_assign_badge_more_than_five_videos(self):
        self.assertEqual(self.user.badges.count(), 0)
        for i in range(6):
            AnimatedVideo.objects.create(title=f'Test Video {i}', uploaded_by=self.user)
        check_collector_status_and_assign_badge(self.user)
        self.assertEqual(self.user.badges.count(), 1)


class TestRemoveCollectorBadge(TestCase):
    def setUp(self):
        self.user = CustomeUser.objects.create(username='testuser', email='test@example.com', password='password')
        self.badge = Badge.objects.create(name="Collectionneur", description="Attribué pour avoir téléverser plus de 5 vidéos")
        self.user.badges.add(self.badge)

    def test_remove_collector_badge(self):
        self.assertEqual(self.user.badges.count(), 1)
        remove_collector_badge(self.user)
        self.assertEqual(self.user.badges.count(), 0)
    
    
