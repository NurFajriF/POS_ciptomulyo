from pickle import FALSE
from django.shortcuts import redirect, render
from django.http import HttpResponse
from flask import jsonify
from django.db.models import Count, Sum
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json, sys
from kategori.models import Kategori
from barang.models import Barang
from penjualan.models import Penjualan, penjualanItem
from datetime import date, datetime

# Create your views here.

@login_required
def daftarPenjualan(request):
    penjualan = Penjualan.objects.all()
    penjualan_data = []
    for jual in penjualan:
        data = {}
        for field in jual._meta.get_fields(include_parents=False):
            if field.related_model is None:
                data[field.name] = getattr(jual,field.name)
        data['items'] = penjualanItem.objects.filter(penjualan_id = jual).all()
        data['item_count'] = len(data['items'])
        
        penjualan_data.append(data)

    context = {
        'page_title':'Transaksi Penjualan',
        'penjualan_data':penjualan_data,
    }
    return render(request, 'penjualan.html',context)

@login_required
def receipt(request):
    id = request.GET.get('id')
    penjualan = Penjualan.objects.filter(id = id).first()
    transaksi = {}
    for field in Penjualan._meta.get_fields():
        if field.related_model is None:
            transaksi[field.name] = getattr(penjualan,field.name)
    itemList = penjualanItem.objects.filter(penjualan_id = penjualan).all()
    context = {
        "transaksi" : transaksi,
        "penjualanItem" : itemList
    }

    return render(request, 'receipt.html',context)

@login_required
def delete_penjualan(request):
    resp = {'status':'failed', 'msg':''}
    id = request.POST.get('id')
    try:
        delete = Penjualan.objects.filter(id = id).delete()
        resp['status'] = 'success'
        messages.success(request, 'Data penjualan berhasil dihapus')
    except:
        resp['msg'] = "An error occured"
        print("Unexpected error:", sys.exc_info()[0])
    return HttpResponse(json.dumps(resp), content_type='application/json')
