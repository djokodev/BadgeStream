from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import VideoUploadForm
from .models import AnimatedVideo
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'video/home.html'

class VideoUploadView(CreateView):
    model = AnimatedVideo
    form_class = VideoUploadForm
    template_name = 'video/upload_video.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Vidéo téléversée avec succès!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erreur lors du téléversement de la vidéo.')
        return super().form_invalid(form)