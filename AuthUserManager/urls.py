from django.urls import path
from django.contrib.auth import views as auth_views
from AuthUserManager.views import SignUpView, SignInView, ProfilView

urlpatterns = [
    path('singin/', SignInView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', ProfilView.as_view(), name='profile'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='AuthUserManager/password_change.html'), name='password_change'),
]
