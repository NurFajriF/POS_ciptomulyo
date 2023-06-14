from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.hutang, name="hutang-page"),
    path('manage_hutang', views.manage_hutang, name="manage_hutang-page"),
    path('save_hutang', views.save_hutang, name="save-hutang-page"),
    path('delete_hutang', views.delete_hutang, name="delete-hutang"),
]