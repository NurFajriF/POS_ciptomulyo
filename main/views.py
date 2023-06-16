from pickle import FALSE
from django.shortcuts import redirect, render
from django.http import HttpResponse
from flask import jsonify
from django.db.models import Count, Sum
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import json, sys
from django.template import loader
from datetime import date, datetime
from barang.models import Barang
from hutang.models import Hutang
from kategori.models import Kategori
from penjualan.models import Penjualan

# Create your views here.

@login_required
def main(request):
    '''function untuk menampilkan report barang, kategori, transaksi, penjualan, dan penghutang harian'''
    now = datetime.now()
    current_year = now.strftime("%Y")
    current_month = now.strftime("%m")
    current_day = now.strftime("%d")
    kategori = len(Kategori.objects.all())
    barang = len(Barang.objects.all())
    transaksi = len(Penjualan.objects.filter(
        date_added__year=current_year,
        date_added__month = current_month,
        date_added__day = current_day
    ))
    penjualan_hari_ini = Penjualan.objects.filter(
        date_added__year=current_year,
        date_added__month = current_month,
        date_added__day = current_day
    ).all()
    total_penjualan = sum(penjualan_hari_ini.values_list('total',flat=True))

    hutang = len(Hutang.objects.all())
    template = loader.get_template('index.html')
    context = {
        'page_title':'Home',
        'kategori' : kategori,
        'barang' : barang,
        'transaksi' : transaksi,
        'total_penjualan' : total_penjualan,
        'hutang' : hutang
    }
    return render(request, 'index.html', context )
