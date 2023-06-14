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

# Create your views here.

# def main(request):
#   template = loader.get_template('index.html')
#   return HttpResponse(template.render())
@login_required
def main(request):
    now = datetime.now()
    current_year = now.strftime("%Y")
    current_month = now.strftime("%m")
    current_day = now.strftime("%d")
    # categories = len(Category.objects.all())
    # products = len(Products.objects.all())
    # transaction = len(Sales.objects.filter(
    #     date_added__year=current_year,
    #     date_added__month = current_month,
    #     date_added__day = current_day
    # ))
    # today_sales = Sales.objects.filter(
    #     date_added__year=current_year,
    #     date_added__month = current_month,
    #     date_added__day = current_day
    # ).all()
    # total_sales = sum(today_sales.values_list('grand_total',flat=True))
    template = loader.get_template('index.html')
    context = {
        'page_title':'Home',
        # 'categories' : categories,
        # 'products' : products,
        # 'transaction' : transaction,
        # 'total_sales' : total_sales,
    }
    return render(request, 'index.html', context )
