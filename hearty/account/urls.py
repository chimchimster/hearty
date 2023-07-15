from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('<int:pk>/', views.AccountDetailView.as_view(), name='account-detail'),
    path('change-email/', views.ChangeEmailView.as_view(), name='change-email'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout')
]