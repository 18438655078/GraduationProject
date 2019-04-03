from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    # url(r'^(\d+)/$', views.detail),
    # 卖家后台登录页面显示
    # url(r'^login/', views.login, name='login'),

    # 卖家后台登录提交操作
    url(r'^dologin/', views.dologin, name='dologin'),

    # 显示商品后台管理页面
    url(r'main/', views.main),

    # 退出
    url(r'^loginout/', views.loginout, name='loginout')
]
