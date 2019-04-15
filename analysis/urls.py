from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^reg/', views.user_register, name='user_register'),
    # url(r'', views.user_register, name='user_register'),
    # 处理表格
    url(r'^do_excel/(?P<id>\d+)', views.do_excel, name='do_excel'),
    url(r'^attention/', views.attention, name='attention'),

]
