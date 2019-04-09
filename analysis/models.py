from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils.html import format_html

class Order(models.Model):
    class Meta:
        verbose_name='订单'
        verbose_name_plural='订单'
    order_file=models.FileField("订单excel",upload_to="uploads",default='')
    dishes_file=models.FileField("菜品excel",upload_to="uploads",default='')
    order = models.CharField(max_length=20, unique=True, verbose_name='订单编号')
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户')
    create_time=models.DateField(auto_now_add=True,verbose_name="创建事件")

    def orderinfo(self):
        color_code = 'green'
        return format_html(
            '<span><a href="" style="color:{};">{}<a></span>', color_code, '查看详情',
        )
    orderinfo.short_description = u'订单详情'
