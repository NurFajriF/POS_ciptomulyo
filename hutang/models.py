from django.db import models
from datetime import datetime
from unicodedata import category
from django.utils import timezone

# Create your models here.

class Hutang(models.Model):
    name = models.TextField()
    total = models.FloatField(default=0)
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True)
