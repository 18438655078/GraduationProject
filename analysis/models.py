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
    img1=models.CharField("销量前15",max_length=100,default='')
    img2=models.CharField("销量后15",max_length=100,default='')
    img3=models.CharField("每天客流量",max_length=100,default='')
    avgcount = models.CharField(max_length=100,verbose_name='平均每桌消费',default='')
    menavg = models.CharField(max_length=100,verbose_name='人均消费',default='')
    dishe_avg = models.CharField(max_length=100,verbose_name='平均菜价',default='')
    use_time = models.CharField(max_length=100,verbose_name='就餐时长',default='')
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户')
    create_time=models.DateField(auto_now_add=True,verbose_name="创建时间")
    is_activate=models.BooleanField("是否解析",default=0)

    def orderinfo(self):
        color_code = 'green'
        return format_html(
            '<span><a href="/analysis/do_excel/{}" style="color:{};">{}<a></span>', self.id, color_code, '查看详情',
        )
    orderinfo.short_description = u'订单详情'
