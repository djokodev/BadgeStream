from django.db import models

class Badge(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images_badges/')
    description = models.TextField()

    def __str__(self):
        return self.name