from django.contrib import admin
from ourapp.models import *
# Register your models here.


class category(admin.ModelAdmin):
    list_display = ['id','category_name']

class cartview(admin.ModelAdmin):
    list_display = ['id','total_amount']

class cartproductview(admin.ModelAdmin):
    list_display = ['id','item','qty','price']  

class supplier(admin.ModelAdmin):
    list_display = ['id','company_name','company_phnumber']


class customer(admin.ModelAdmin):
    list_display = ['id', 'user', 'phone', 'address']


class stockHistory(admin.ModelAdmin):
    list_display = ('item', 'supplier','action', 'quantity', 'date', 'note')
    list_filter = ('supplier','action', 'date')
    search_fields = ('item__item_name', 'supplier__name', 'note')





admin.site.register(Category,category)
admin.site.register(Disease)
admin.site.register(Supplier,supplier)
admin.site.register(Item)
admin.site.register(Cart,cartview)
# admin.site.register(CartItem)
# admin.site.register(StockHistory)
admin.site.register(Sale)
admin.site.register(SaleItem)
admin.site.register(Customer,customer)
admin.site.register(StockHistory,stockHistory)






