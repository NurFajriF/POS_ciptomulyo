from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.barang, name="barang-page"),
    path('manage_barang', views.manage_barang, name="manage_barang-page"),
    path('save_barang', views.save_barang, name="save-barang-page"),
    path('delete_barang', views.delete_barang, name="delete-barang"),
]