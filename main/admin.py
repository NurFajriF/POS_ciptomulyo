from django.contrib import admin
from barang.models import Barang
from kategori.models import Kategori

# Register your models here.
admin.site.register(Barang)
admin.site.register(Kategori)
