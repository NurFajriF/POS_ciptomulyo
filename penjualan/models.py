from datetime import datetime
from unicodedata import category
from django.db import models
from django.utils import timezone
from barang.models import Barang

# Create your models here.

class Penjualan(models.Model):
    code = models.CharField(max_length=100)
    total = models.FloatField(default=0)
    tendered_amount = models.FloatField(default=0)
    amount_change = models.FloatField(default=0)
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.code

class penjualanItem(models.Model):
    penjualan_id = models.ForeignKey(Penjualan,on_delete=models.CASCADE)
    barang_id = models.ForeignKey(Barang,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    qty = models.FloatField(default=0)
    total = models.FloatField(default=0)
