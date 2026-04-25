from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.users.models import User


# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass
