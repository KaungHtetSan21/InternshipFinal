"""
URL configuration for ourproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ourapp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeview, name= 'homeview'),
     path('register/', customer_register, name='customer_register'),

    path('loginview/', loginview, name= 'loginview'),
    path('logoutview/', logoutview, name= 'logoutview'),
    path('medgrid4/', medgrid4, name= 'medgrid4'),
    path('medgrid5/', medgrid5, name= 'medgrid5'),
    path('medlist/<int:id>/', medlist, name= 'medlist'),
    # path('sendmsg/', sendmsg, name= 'sendmsg'),
    path('medicinedetail/<int:id>/', meddetail, name='meddetail'),
    path('deleteitem/<int:id>/', deleteitem, name= 'deleteitem'),
    path('deletedisease/<int:id>/', deletedisease, name= 'deletedisease'),

    path('medicineview/', medview, name= 'medview'),
    path('diseaseview/', dis_view, name= 'dis_view'),
    path('addproduct/', addproduct, name= 'addproduct'),
    path('adddisease/', adddisease, name= 'adddisease'),
    path('addsupplier/', addsupplier, name= 'addsupplier'),
    path('companyview/', companyview, name= 'companyview'),
    path('supvounchar/', supvounchar, name= 'supvounchar'),

    path('diseaseupdateview/<int:id>/', dis_updateview, name= 'dis_updateview'),
    path('medicineupdateview/<int:id>/', med_updateview, name= 'med_updateview'),
    path('stockin/', stock_in, name= 'stock_in'),

    
    # path('addtocart/<int:id>/',addtocart, name='addtocart'),
    # path('cartview/', cartView, name= 'cartView'),
    # path('cart/increase/<int:id>/',increase_qty, name='increase_qty'),
    # path('cart/decrease/<int:id>/', decrease_qty, name='decrease_qty'),
    # path('cart/remove/<int:cart_item_id>/',remove_cart_item, name='remove_cart_item'),
    # path('cartlist/',cart_list , name= 'cart_list'),
    # path('cart/add/<int:item_id>/',add_to_cart , name= 'add_to_cart'),
    # path('update-cart-qty/<int:item_id>/', update_cart_qty, name='update_cart_qty'),

    path('checkout/',checkout , name= 'checkout'),
    path('cart/add/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('cart/increase/<int:item_id>/', increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:item_id>/', decrease_quantity, name='decrease_quantity'),
    path('cart/remove/<int:item_id>/',remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:item_id>/',update_quantity, name='update_quantity'),
    path('cart/clear/', clear_cart, name='clear_cart'),
    
 
    path('cartlist/', cart_list, name='cart_list'),
    path('report/daily/', daily_sales_report, name='daily_sales_report'),
    path('report/monthly/',monthly_sales_report, name='monthly_sales_report'),
    path('report/yearly/', yearly_sales_report, name='yearly_sales_report'),
    path('promotion-items/', promotion_items, name='promotion_items'),
]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)