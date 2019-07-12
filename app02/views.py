# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from app02 import models
from django.shortcuts import render,HttpResponse,redirect

from django.views import View
from django.urls import reverse

# Create your views here.
def index(request):
    return  render(request,"index.html")

def publish_list(request):
    pubobjs=models.Publishernew.objects.all()
    return render(request,'publish_list.html',{"pubobjs":pubobjs})

def book_list(request):
    bookobjs=models.Booknew.objects.all()
    return render(request,'book_list.html',{"bookobjs":bookobjs})

class Addpub(View):
    def get(self,request):
        return render(request,"add_publish.html")
    def post(self,request):
        print(request.POST)
        return HttpResponse("ok")

def delete(request,table,id):
    print(table)
    print(id)
    tablename=table.capitalize()
    obj=getattr(models,tablename)
    obj.objects.filter(pid=id).first().delete()
    return redirect(reverse("app02:publishnew",args=()))





