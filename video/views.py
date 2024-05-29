from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import VideoUploadForm
from .models import AnimatedVideo
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.exceptions import ValidationError


class HomeView(LoginRequiredMixin, ListView):
    model= AnimatedVideo
    template_name = 'video/home.html'
    context_object_name = 'videos'

class VideoUploadView(CreateView):
    model = AnimatedVideo
    form_class = VideoUploadForm
    template_name = 'video/upload_video.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        try:
            instance = form.save(commit=False)
            instance.uploaded_by = self.request.user
            instance.save()
            messages.success(self.request, 'Vidéo téléversée avec succès!')
            return super().form_valid(form)
        except ValidationError as e:
            for message in e.messages:
                messages.error(self.request, message)
            return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erreur lors du téléversement de la vidéo.')
        return super().form_invalid(form)
    
class VideoDetailView(DetailView):
    model = AnimatedVideo
    template_name = 'video/video_detail.html' 
    context_object_name = 'video'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class VideoDeleteView(LoginRequiredMixin, DeleteView):
    model = AnimatedVideo
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return self.model.objects.filter(uploaded_by=self.request.user)