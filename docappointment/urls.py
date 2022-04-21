from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/register/', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('edit-profile', views.editProfile, name='edit-profile'),
]
