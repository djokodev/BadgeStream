from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.models import AbstractUser

class CustomeUser(AbstractUser):
    email = models.EmailField(unique=True, validators=[EmailValidator(message="Invalid email address")])