from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.http import HttpResponse


def login(request):
    return render(request, 'gapp/login.html')


def do_login(request):
    pass


def index(request):
    return HttpResponse("123456789")


def detail(num):
    return HttpResponse("detail-%s" % num)
