from django.contrib import admin
from .models import Profile, Images


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ['pk', 'user', 'description', 'gender', 'preferences']


@admin.register(Images)
class AdminImage(admin.ModelAdmin):
    list_display = ['profile', 'image']