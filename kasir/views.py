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
from barang.models import Barang
from kategori.models import Kategori
from penjualan.models import Penjualan, penjualanItem
from datetime import date, datetime

# Create your views here.
@login_required
def kasir(request):
    barang = Barang.objects.all()
    bar_json = []
    for bar in barang:
        bar_json.append({'id':bar.id, 'name':bar.name, 'price':float(bar.price)})
    context = {
        'page_title' : "Kasir",
        'barang' : barang,
        'bar_json' : json.dumps(bar_json)
    }
    # return HttpResponse('')
    return render(request, 'kasir.html',context)

@login_required
def checkout_modal(request):
    final_total = 0
    if 'final_total' in request.GET:
        final_total = request.GET['final_total']
    context = {
        'final_total' : final_total,
    }
    return render(request, 'checkout.html',context)

@login_required
def save_kasir(request):
    resp = {'status':'failed','msg':''}
    data = request.POST
    pref = datetime.now().year + datetime.now().year
    i = 1
    while True:
        code = '{:0>5}'.format(i)
        i += int(1)
        check = Penjualan.objects.filter(code = str(pref) + str(code)).all()
        if len(check) <= 0:
            break
    code = str(pref) + str(code)

    try:
        penjualan = Penjualan(code=code, total = data['final_total'], tendered_amount = data['tendered_amount'], amount_change = data['amount_change']).save()
        penjualan_id = Penjualan.objects.last().pk
        i = 0
        for bar in data.getlist('barang_id[]'):
            barang_id = bar 
            jual = Penjualan.objects.filter(id=penjualan_id).first()
            barang = Barang.objects.filter(id=barang_id).first()
            qty = data.getlist('qty[]')[i] 
            price = data.getlist('price[]')[i] 
            total = float(qty) * float(price)
            print({'penjualan_id' : jual, 'barang_id' : barang, 'qty' : qty, 'price' : price, 'total' : total})
            penjualanItem(penjualan_id = jual, barang_id = barang, qty = qty, price = price, total = total).save()
            i += int(1)
        resp['status'] = 'success'
        resp['penjualan_id'] = penjualan_id
        messages.success(request, "Data penjualan berhasil disimpan")
    except:
        resp['msg'] = "An error occured"
        print("Unexpected error:", sys.exc_info()[0])
    return HttpResponse(json.dumps(resp),content_type="application/json")

@login_required
def receipt(request):
    id = request.GET.get('id')
    penjualan = Penjualan.objects.filter(id = id).first()
    transaksi = {}
    for field in Penjualan._meta.get_fields():
        if field.related_model is None:
            transaksi[field.name] = getattr(penjualan,field.name)
    penjualanItem = penjualanItem.objects.filter(penjualan_id = penjualan).all()
    context = {
        "transaksi" : transaksi,
        "penjualanItem" : penjualanItem
    }

    return render(request, 'receipt.html',context)
