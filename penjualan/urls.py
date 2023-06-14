from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', views.daftarPenjualan, name="penjualan-page"),
    path('receipt', views.receipt, name="receipt-modal"),
    path('delete_penjualan', views.delete_penjualan, name="delete-penjualan"),
]
