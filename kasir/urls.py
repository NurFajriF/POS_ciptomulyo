from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.kasir, name="kasir-page"),
    path('checkout-modal', views.checkout_modal, name="checkout-modal"),
    path('save-kasir', views.save_kasir, name="save-kasir"),
    path('receipt', views.receipt, name="receipt-modal"),
]
