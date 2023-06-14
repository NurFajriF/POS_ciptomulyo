from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.kategori, name="kategori-page"),
    path('manage_kategori', views.manage_kategori, name="manage_kategori-page"),
    path('save_kategori', views.save_kategori, name="save-kategori-page"),
    path('delete_kategori', views.delete_kategori, name="delete-kategori"),
]