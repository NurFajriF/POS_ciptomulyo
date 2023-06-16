from django.contrib import admin
from barang.models import Barang
from hutang.models import Hutang
from kategori.models import Kategori
from penjualan.models import Penjualan

# Register your models here.
admin.site.register(Barang)
admin.site.register(Hutang)
admin.site.register(Kategori)
admin.site.register(Penjualan)
