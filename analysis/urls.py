from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.user_login, name='login'),
    url(r'^register/', views.user_register, name='register'),
    url(r'^logout/', views.user_logout, name='logout'),
    # url(r'^(\d+)/$', views.detail),
    # 卖家后台登录页面显示
    # url(r'^login/', views.login, name='login'),

    # 显示商品后台管理页面
    url(r'index/', views.index, name='index'),
    # 处理表格
    url(r'^do_excel/', views.do_excel, name='do_excel'),
]
