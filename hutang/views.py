from pickle import FALSE
from django.shortcuts import redirect, render
from django.http import HttpResponse
from flask import jsonify
from django.db.models import Count, Sum
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json, sys
from .models import Hutang
from datetime import date, datetime

# Create your views here.

#Hutang
@login_required
def hutang(request):
    hut_list = Hutang.objects.all()
    context = {
        'page_title':'Daftar Hutang',
        'hutang':hut_list,
    }
    return render(request, 'hutang.html',context)

@login_required
def manage_hutang(request):
    hutang = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            hutang = Hutang.objects.filter(id=id).first()
    
    context = {
        'hutang' : hutang
    }
    return render(request, 'manage_hutang.html',context)

@login_required
def save_hutang(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_hutang = Hutang.objects.filter(id = data['id']).update(name=data['name'], total = data['total'],)
        else:
            save_hutang = Hutang(name=data['name'], total = data['total'])
            save_hutang.save()
        resp['status'] = 'success'
        messages.success(request, 'Hutang berhasil disimpan.')
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_hutang(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Hutang.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
        messages.success(request, 'Hutang berhasil dilunasi & dihapus.')
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

