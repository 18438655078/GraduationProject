from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/', views.user_register, name='user_register'),
    # 处理表格
    url(r'^do_excel/', views.do_excel, name='do_excel'),
]
