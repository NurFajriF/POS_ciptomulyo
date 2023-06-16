from pickle import FALSE
from django.shortcuts import redirect, render
from django.http import HttpResponse
from flask import jsonify
from .models import Barang
from kategori.models import Kategori
from django.db.models import Count, Sum
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json, sys
from datetime import date, datetime


# Barang
@login_required
def barang(request):
    '''function untuk mengambil data barang dari tabel barang dan menampilkannya'''
    bar_list = Barang.objects.all()
    context = {
        'page_title':'Daftar Barang',
        'barang':bar_list,
    }
    return render(request, 'barang.html',context)

@login_required
def manage_barang(request):
    '''function untuk mengambil data barang dari tabel berdasarkan id nya untuk diedit'''
    bar = {}
    kategori = Kategori.objects.all()
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            bar = Barang.objects.filter(id=id).first()
    
    context = {
        'bar' : bar,
        'kategori' : kategori
    }
    return render(request, 'manage_barang.html',context)

@login_required
def save_barang(request):
    '''function untuk memasukkan data barang yang dibuat ke tabel barang'''
    data =  request.POST
    resp = {'status':'failed'}
    id= ''
    if 'id' in data:
        id = data['id']
    if id.isnumeric() and int(id) > 0:
        check = Barang.objects.exclude(id=id).filter(code=data['code']).all()
    else:
        check = Barang.objects.filter(code=data['code']).all()
    if len(check) > 0 :
        resp['msg'] = "Barang tersebut sudah ada!"
    else:
        kategori = Kategori.objects.filter(id = data['kategori_id']).first()
        try:
            if (data['id']).isnumeric() and int(data['id']) > 0 :
                save_barang = Barang.objects.filter(id = data['id']).update(code=data['code'], kategori_id=kategori, name=data['name'], merk = data['merk'], price = float(data['price']))
            else:
                save_barang = Barang(code=data['code'], kategori_id=kategori, name=data['name'], merk = data['merk'], price = float(data['price']))
                save_barang.save()
            resp['status'] = 'success'
            messages.success(request, 'Barang berhasil disimpan.')
        except:
            resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_barang(request):
    '''function untuk menghapus data barang berdasarkan id yang dipilih'''
    data =  request.POST
    resp = {'status':''}
    try:
        Barang.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
        messages.success(request, 'Barang berhasil dihapus.')
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")
