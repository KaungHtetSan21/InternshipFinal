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
from chatapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeview, name= 'homeview'),
    path('registerview/', registerview, name= 'registerview'),
    path('loginview/', loginview, name= 'loginview'),
    path('logoutview/', logoutview, name= 'logoutview'),
    path('medgrid4/', medgrid4, name= 'medgrid4'),
    path('medgrid5/', medgrid5, name= 'medgrid5'),
    path('medlist/<int:id>/', medlist, name= 'medlist'),
    path('sendmsg/', sendmsg, name= 'sendmsg'),
    path('medicinedetail/<int:id>/', meddetail, name='meddetail'),
    path('deleteitem/<int:id>/', deleteitem, name= 'deleteitem'),
    path('deletedisease/<int:id>/', deletedisease, name= 'deletedisease'),

    path('medicineview/', medview, name= 'medview'),
    path('diseaseview/', dis_view, name= 'dis_view'),
    path('addproduct/', addproduct, name= 'addproduct'),
    path('adddisease/', adddisease, name= 'adddisease'),
    path('diseaseupdateview/<int:id>/', dis_updateview, name= 'dis_updateview'),
    path('medicineupdateview/<int:id>/', med_updateview, name= 'med_updateview'),
    
    # path('addtocart/<int:id>/',addtocart, name='addtocart'),
    # path('cartview/', cartView, name= 'cartView'),
    # path('cart/increase/<int:id>/',increase_qty, name='increase_qty'),
    # path('cart/decrease/<int:id>/', decrease_qty, name='decrease_qty'),
    path('cart/remove/<int:cart_item_id>/',remove_cart_item, name='remove_cart_item'),
    path('cartlist/',cart_list , name= 'cart_list'),
    path('cart/add/<int:item_id>/',add_to_cart , name= 'add_to_cart'),
    path('checkoutview/',checkoutview , name= 'checkoutview'),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)