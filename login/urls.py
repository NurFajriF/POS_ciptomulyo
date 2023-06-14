from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name = 'login.html',redirect_authenticated_user=True), name="login"),
]
