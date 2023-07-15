from django.urls import path
from . import views


app_name = 'profiles'

urlpatterns = [
    path('<int:pk>/', views.ProfileView.as_view(), name='profile_view'),
    path('upload_image/', views.UploadImageView.as_view(), name='upload_image'),
    path('delete_image/', views.DeleteImageView.as_view(), name='delete_image'),
    path('swipes/', views.Swipes.as_view(), name='swipes'),
    path('like/', views.ProfileLikeView.as_view(), name='like'),
    path('dislike/', views.ProfileDislikeView.as_view(), name='dislike'),
    path('my_sympathy/', views.ProfileOwnSympathyView.as_view(), name='my_sympathy'),
    path('other_sympathy/', views.ProfileOtherSympathyView.as_view(), name='other_sympathy'),
    path('notification_has_been_read/<int:notification_id>', views.mark_notification_as_read, name='notification_has_been_read'),
]