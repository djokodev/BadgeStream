from django.urls import path
from django.contrib.auth import views as auth_views
from AuthUserManager.views import SignUpView, SignInView, ProfilView, DeleteAccountView

urlpatterns = [
    path('singin/', SignInView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', ProfilView.as_view(), name='profile'),
    path('delete-account/<int:pk>/', DeleteAccountView.as_view(), name='delete_account'),
    
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='AuthUserManager/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='AuthUserManager/password_change_done.html'), name='password_change_done'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='AuthUserManager/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='AuthUserManager/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='AuthUserManager/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='AuthUserManager/password_reset_complete.html'), name='password_reset_complete'),
]
