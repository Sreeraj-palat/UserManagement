import imp
from math import prod
from multiprocessing import context
from types import MethodType
from django.contrib import messages
from turtle import home
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model

from user.models import Item
import os

# Create your views here.

# def user_home(request):
#     return render(request,'user_home.html')

def user_login(request):
    if 'username' in request.session :
        return redirect(user_home)
    if request.method == 'POST' :
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(username=username, password=password)
         if user is not None :
            #  if request.user.is_superuser:
                 request.session['username'] = username
                 return redirect(user_home)
     
         else :
             messages.error(request,'invalid username or password')
             print('invaid credentials')
    return render(request,'user.html')  


def user_home(request):  
    q= request.GET.get('q') if request.GET.get('q') != None else ''
    products = Item.objects.filter()
    context = {'products': products}
    return render(request,'user_home.html', context)

    if 'username' in request.session :

        return render(request, 'user_home.html')
    else:

        return redirect(user_login)    

def user_logout(request):
    if 'username' in request.session :
        request.session.flush()
    return redirect(user_login)  



def reg_user(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']


        if password1==password2:
            if User.objects.filter(username=username).exists():
                print('user name taken')
            elif User.objects.filter(email=email).exists():
                print('email taken')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name, last_name=last_name)    
                user.save()
                print('user created')
                return redirect(user_login) 


    else:
        return render(request,'reg_user.html')  



def add_product(request):
    if request.method == "POST":
        prod = Item()
        prod.name = request.POST.get('name')
        prod.description = request.POST.get('description')
        prod.price = request.POST.get('price')

        if len(request.FILES) != 0:
            prod.image = request.FILES['image']

        prod.save()
        messages.success(request,"Product Added Succesfully")
        return redirect(user_home)    

    return render(request,'add_product.html')   

def edit_product(request, pk):
    prod = Item.objects.get(id=pk)

    if request.method == "POST":
        if len(request.FILES) !=0:
            if len(prod.image) > 0:
                os.remove(prod.image.path)
        prod.name = request.POST.get('name')
        prod.description = request.POST.get('description')
        prod.price = request.POST.get('price')
        prod.save()
        messages.success(request, "Product updated successfully")
        return redirect(user_home)       
    context = {'prod':prod}
    return render (request,'edit_product.html',context)


def delete_product(request,pk):
    prod = Item.objects.filter(id=pk)
    prod.delete()
    messages.success(request,"Product deleted successfully")
    return redirect(user_home)

