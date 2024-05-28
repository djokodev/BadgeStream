from django.db import models
from AuthUserManager.models import CustomeUser

class AnimatedVideo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)


    def __str__(self):
        return self.title