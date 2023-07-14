from django.contrib import admin
from .models import Profile, Images, Cities, Countries, Like, Dislike


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ['pk', 'user', 'description', 'gender', 'preferences']


@admin.register(Images)
class AdminImage(admin.ModelAdmin):
    list_display = ['profile', 'image']


@admin.register(Cities)
class AdminCity(admin.ModelAdmin):
    list_display = ['city', 'country_id']
    list_filter = ['city', 'country_id']


@admin.register(Countries)
class AdminCountry(admin.ModelAdmin):
    list_display = ['country']


@admin.register(Like)
class AdminLike(admin.ModelAdmin):
    list_display = ['sender', 'receiver']


@admin.register(Dislike)
class AdminDislike(admin.ModelAdmin):
    list_display = ['sender', 'receiver']