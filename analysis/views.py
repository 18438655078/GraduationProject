from django.shortcuts import render
from django.http import HttpResponseRedirect
import pandas as pd
from django.contrib.auth.models import User,Group
from django.contrib.auth import login as Auth_Login,authenticate,logout as Auth_Logout
from .models import Order

def user_register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if user.exists():
            return render(request, 'register.html',{'msg': '账号已存在'})
        else:
            group = Group.objects.get(name="用户")
            u=User.objects.create_user(username=username, password=password,is_staff=1)
            u.groups.add(group)
            Auth_Logout(request)
            return HttpResponseRedirect('/admin')

def do_excel(request):
    # 读取表格处理数据
    order_file = request.FILES.get('order_file')
    dishes_file = request.FILES.get('dishes_file')
    order_file_data = pd.read_excel(order_file)
    dishes_file_data = pd.read_excel(dishes_file)
