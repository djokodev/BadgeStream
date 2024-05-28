from django.urls import path
from video.views import HomeView, VideoUploadView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('upload/', VideoUploadView.as_view(), name='upload_video'),
]
