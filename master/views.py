from multiprocessing import context
from pdb import post_mortem
from unicodedata import name
from django.contrib import messages
from turtle import home
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model

import user
from django.db.models import Q

# Create your views here.


# def index(request):
#     return render(request,'index.html')

def master_login(request):
    if 'username' in request.session :
        return redirect(master_home)
    if request.method == 'POST' :
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(username=username, password=password)
         if user is not None :
             if user.is_superuser:
                 request.session['username'] = username
                 return redirect(master_home)
     
         else :
             messages.error(request,'invalid username or password')
             print('invaid credentials')
    return render(request,'master.html')   


def master_home(request):  
    # if user.is_superuser:
         if 'username' in request.session :

             return render(request, 'master_home.html')
         else:

             return redirect(master_login)    

def master_logout(request):
    if 'username' in request.session :
        request.session.flush()
    return redirect(master_login)  


def add_user(request):
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
                return redirect(add_user)    

    else:
        return render(request,'add_user.html')   


def view_user(request):

    q= request.GET.get('q') if request.GET.get('q') != None else ''
    Users = get_user_model()
    users = Users.objects.filter(
        Q(username__icontains=q)|
        Q(id__icontains=q)|
        Q(email__icontains=q)|
        Q(first_name__icontains=q)|
        Q(last_name__icontains=q)
    )
    context = {'users':users}
    return render(request,'view_user.html',context)


def edit_user(request,id):
    user = User.objects.get(id=id)
    context = {'user':user}
    if request.method == "POST":
        user.username = request.POST['username']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        messages.success(request,'Successfully Changed')
        return redirect(view_user)
    return render(request,'edit_user.html',context)    


def delete_user(request,id):
    user=User.objects.filter(id=id)
    user.delete()
    return redirect(view_user)







             
    
