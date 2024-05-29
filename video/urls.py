from django.urls import path
from video.views import HomeView, VideoUploadView, VideoDetailView, VideoDeleteView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('upload/', VideoUploadView.as_view(), name='upload_video'),
    path('video/<int:pk>/', VideoDetailView.as_view(), name='video_detail'),
    path('video/<int:pk>/delete/', VideoDeleteView.as_view(), name='video_delete'),
]
