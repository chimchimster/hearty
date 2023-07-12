from django.urls import path
from .views import ProfileView, UploadImageView

app_name = 'profiles'

urlpatterns = [
    path('<int:pk>/', ProfileView.as_view(), name='profile_view'),
    path('upload_image/', UploadImageView.as_view(), name='upload_image'),
]