from pickle import FALSE
from django.shortcuts import redirect, render
from django.http import HttpResponse
from flask import jsonify
from .models import Kategori
from django.db.models import Count, Sum
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json, sys
from datetime import date, datetime

# Create your views here.

#Kategori
@login_required
def kategori(request):
    kat_list = Kategori.objects.all()
    context = {
        'page_title':'Daftar Kategori',
        'kategori':kat_list,
    }
    return render(request, 'kategori.html',context)

@login_required
def manage_kategori(request):
    kategori = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            kategori = Kategori.objects.filter(id=id).first()
    
    context = {
        'kategori' : kategori
    }
    return render(request, 'manage_kategori.html',context)

@login_required
def save_kategori(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_kategori = Kategori.objects.filter(id = data['id']).update(name=data['name'], description = data['description'],)
        else:
            save_kategori = Kategori(name=data['name'], description = data['description'])
            save_kategori.save()
        resp['status'] = 'success'
        messages.success(request, 'Kategori berhasil disimpan.')
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_kategori(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Kategori.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
        messages.success(request, 'Kategori berhasil dihapus.')
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

