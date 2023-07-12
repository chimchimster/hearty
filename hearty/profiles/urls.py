from django.urls import path
from .views import ProfileView, UploadImageView, DeleteImageView

app_name = 'profiles'

urlpatterns = [
    path('<int:pk>/', ProfileView.as_view(), name='profile_view'),
    path('upload_image/', UploadImageView.as_view(), name='upload_image'),
    path('delete_image/', DeleteImageView.as_view(), name='delete_image'),
]