from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import pandas as pd
from .models import UserInfo

# Create your views here.

from django.shortcuts import render, redirect
from .models import UserProfile
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, UserLoginForm


def user_register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        # 实例form类，用来验证用户提交的数据
        user_register_form = UserRegisterForm(request.POST)
        if user_register_form.is_valid():  # 返回值为True或False
            username = user_register_form.cleaned_data['username']
            password = user_register_form.cleaned_data['password']

            user = UserProfile.objects.filter(username=username)
            if user:
                return render(request, 'register.html', {
                    'mag': '账号已存在'
                })
            else:
                a = UserProfile()
                a.password = password
                a.username = username
                # 内部函数自动加密功能
                a.set_password(password)
                a.save()
                return redirect(reverse('login'))
        else:
            return render(request, 'register.html', {
                'user_register_form': user_register_form
            })


def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():
            username = user_login_form.cleaned_data['username']
            password = user_login_form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('index'))

            else:
                return render(request, 'login.html', {
                    'msg': '用户名或者密码错误！',
                    'user_login_form': user_login_form
                })
        else:
            pass


def user_logout(request):
    logout(request)
    return render(request, 'index.html')


#
# def login(request):
#     return render(request, 'gapp/login.html')


def do_login(request):
    username = request.POST['username']
    password = request.POST['password']


def index(request):
    return HttpResponse("123456789")


def detail(request):
    return HttpResponse("detail-%s" % request)


def do_excel(request):
    # 读取表格处理数据
    excel_raw_data = pd.read_excel(request.FILES.get('excel'))