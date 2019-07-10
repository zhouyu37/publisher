# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from app01 import models
# Create your views here.
def index(request):
    return HttpResponse("ok")

def login(request):
    error_msg=""
    if request.method == "POST":
        user=request.POST.get("user")
        pwd=request.POST.get("pwd")
        if user=="alex" and pwd=="123456":
            return redirect("/index")
        else:
            error_msg = "user or password is wrong"
    return render(request,"login.html",{"error_msg":error_msg})

def list_publish(request):
    all_publisher=models.Publisher.objects.all()
    return render(request,'list.html',{"all_publisher":all_publisher})

def add_publish(request):
    error_msg = ""
    if request.method == "POST":
        new=request.POST.get("publisher")
        if len(new) == 0:
            error_msg = "the field can not null"
        else:
            obj=models.Publisher.objects.filter(name=new)
            print("zhou",len(obj))
            if len(obj) > 0:
                error_msg = "the field is existed"
            else:
                obj= models.Publisher.objects.create(name=new)
                return redirect("/list_publish/")
    return render(request, "add.html", {"error_msg": error_msg})

def del_publish(request):
    id=request.GET.get("pk")
    models.Publisher.objects.filter(id=id).delete()
    return redirect("/list_publish/")

def edit_publish(request):
    error_msg = ""
    id = request.GET.get("pk")
    obj= models.Publisher.objects.filter(id=id).first()
    if request.method == "POST":
        new_name=request.POST.get("new_name")
        if len(new_name) == 0:
            error_msg = "new field can not null"
        else:
            obj1=models.Publisher.objects.filter(name=new_name)
            if len(obj1) > 0:
                error_msg = "the row is existed"
            else:
                obj.name=new_name
                obj.save()
                return  redirect("/list_publish/")


    return render(request,"edit.html",{"obj":obj,"error_msg":error_msg})
