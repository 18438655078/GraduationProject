from django.contrib import admin
from .models import Order
import time
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ('user','order','create_time','orderinfo')
	search_fields = ('user','order','create_time',)
	exclude = ('order','user')
	def get_queryset(self, request):
		qs = super(OrderAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(user=request.user)
	def get_readonly_fields(self, request, obj=None):
		if obj:
			return ['user','order','create_time','order_file','dishes_file']
		else:
			return []
	def save_model(self, request, obj, form, change):
		obj.user=request.user
		t = str(time.time()).split('.')
		orders = t[0] + t[1]
		obj.order=orders
		super(OrderAdmin, self).save_model(request, obj, form, change)

admin.site.site_header='餐饮数据分析'
admin.site.site_title='餐饮数据分析'
