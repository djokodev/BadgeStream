from django import forms
from .models import AnimatedVideo

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = AnimatedVideo
        fields = ['title', 'description', 'file', 'thumbnail']