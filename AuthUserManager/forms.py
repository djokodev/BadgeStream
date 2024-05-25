from django import forms
from AuthUserManager.models import CustomeUser
from django.contrib.auth.forms import AuthenticationForm

class CustomeUserRegistrationFrom(forms.ModelForm):
    password1 = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmez le mot de passe', widget=forms.PasswordInput)

    class Meta:
        model = CustomeUser
        fields = ("username", "email")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Les mots de passe ne correspondent pas")
        return password2
    
class CustomeUserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)