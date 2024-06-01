from django.test import TestCase, Client
from video.models import AnimatedVideo
from AuthUserManager.models import CustomeUser
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.core.exceptions import ValidationError


class TestCaseVideo(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomeUser.objects.create(username='testuser', email='test@example.com')
        self.user.set_password('password')
        self.user.save()
        self.video_file = SimpleUploadedFile("testfile.mp4", b"file_content", content_type="video/mp4")
        self.thumbnail_file = SimpleUploadedFile("thumbnail.jpg", b"thumbnail_content", content_type="image/jpeg")
        self.video = AnimatedVideo.objects.create(
            title='Test Video',
            description='This is a test video.',
            file=self.video_file,
            thumbnail=self.thumbnail_file,
            uploaded_by=self.user,
            views=10
        )

    def test_video_creation(self):
        self.assertEqual(self.video.title, 'Test Video')
        self.assertEqual(self.video.description, 'This is a test video.')
        self.assertTrue(self.video.file.name.startswith('video_stream/testfile'))
        self.assertEqual(self.video.uploaded_by, self.user)
        self.assertEqual(self.video.views, 10)

    def test_home_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'video/home.html')

    def test_video_upload_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('upload_video'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'video/upload_video.html')

    def test_video_detail_view(self):
        response = self.client.get(reverse('video_detail', kwargs={'pk': self.video.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'video/video_detail.html')

    def test_video_format_validation(self):
        with self.assertRaises(ValidationError):
            invalid_file = SimpleUploadedFile("invalidfile.txt", b"invalid content", content_type="text/plain")
            AnimatedVideo.objects.create(
                title='Test Video',
                description='This is a test video.',    
                file=invalid_file,
                uploaded_by=self.user
            )
    