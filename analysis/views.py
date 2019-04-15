from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
import pandas as pd
from django.contrib.auth.models import User, Group
from django.contrib.auth import login as Auth_Login, authenticate, logout as Auth_Logout
from django.contrib.auth.decorators import login_required
from .models import Order
from . import data_process


def user_register(request):
    if request.method == 'GET':
        return render(request, 'reg.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if user.exists():
            return render(request, 'reg.html', {'msg': '账号已存在'})
        else:
            group = Group.objects.get(name="用户")
            u = User.objects.create_user(username=username, password=password, is_staff=1)
            u.groups.add(group)
            Auth_Logout(request)
            return HttpResponseRedirect('/admin')


def attention(request):
    return render(request, 'attention.html')


@login_required
def do_excel(request, id):
    # 读取表格处理数据
    print(id)
    order = Order.objects.filter(id=id)
    if not order.exists():
        return Http404
    o = order[0]
    if o.is_activate == 1:
        return render(request, 'show.html', {"order": o})
    order_file = o.order_file.name
    dishes_file = o.dishes_file.name

    print(order_file, order_file)
    # 传入表格url
    item = data_process.deal(dishes_file, order_file)
    img1 = item['img1']
    img2 = item['img2']
    img3 = item['img3']
    avgcount = item['avgcount']
    menavg = item['menavg']
    dishe_avg = item['dishe_avg']
    use_time = item['use_time']
    print(item)
    Order.objects.filter(id=id).update(img1=img1, img2=img2, img3=img3, avgcount=avgcount, menavg=menavg,
                                       dishe_avg=dishe_avg, use_time=use_time, is_activate=1)
    # u = User.objects.create_user(username=username, password=password, is_staff=1)
    # data_process.deal(order_file_data, dishes_file_data)
    order = Order.objects.get(id=id)
    print(order)
    return render(request, 'show.html', {"order": order})
