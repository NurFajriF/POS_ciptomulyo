from django.db import models
from datetime import datetime
from unicodedata import category
from django.utils import timezone
from kategori.models import Kategori
# Create your models here.

class Barang(models.Model):
    code = models.CharField(max_length=100)
    kategori_id = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    name = models.TextField()
    merk = models.TextField()
    price = models.FloatField(default=0)
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.code + " - " + self.name

