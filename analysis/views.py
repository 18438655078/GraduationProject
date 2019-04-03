from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import pandas as pd

# Create your views here.

from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError



def login(request):
    return render(request, 'gapp/login.html')


def do_login(request):
    pass


def index(request):
    return HttpResponse("123456789")


def detail(request):
    return HttpResponse("detail-%s" % request)


def do_excel(request):
    # 读取表格处理数据
    excel_raw_data = pd.read_excel(request.FILES.get('excel'))