from datetime import datetime
from unicodedata import category
from django.db import models
from django.utils import timezone

# Create your models here.


class Kategori(models.Model):
    name = models.TextField()
    description = models.TextField()
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name