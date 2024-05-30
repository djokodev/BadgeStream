from django.contrib import admin
from AuthUserManager.models import CustomeUser

class CustomeUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined')

admin.site.register(CustomeUser, CustomeUserAdmin)