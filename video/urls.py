from django.urls import path
from video.views import home

urlpatterns = [
    path('home/', home, name='home'),
]
