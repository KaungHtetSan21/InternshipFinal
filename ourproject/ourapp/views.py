from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from ourapp.models import *
from django.contrib.auth.models import User
from .models import *
from django.core.paginator import Paginator
from .form import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone


# Create your views here.
def homeview(request):
    return render(request,'index.html')

def registerview(request):
    if request.method == 'POST':
        Username = request.POST['customer[username]']
        password = request.POST['customer[password]']
        
        first_name = request.POST['customer[first_name]']
        last_name = request.POST['customer[last_name]']
        email = request.POST['customer[email]']
        usr = User.objects.filter(username= Username)
        if usr.exists():
            redirect('/register/')
        else:
            user_obj = User.objects.create_user(username=Username, first_name=first_name, last_name=last_name ,email=email )
            user_obj.set_password(password)
            # user_obj.is_staff=True
            user_obj.save()
            return redirect('/')
    else:
        return render(request,'register.html')
    
    


   
def loginview(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'username or password invalid')
            # return render(request, 'login.html', context)
        context ={}
        return render(request, 'login.html', context)
    
def logoutview(request):
    logout(request)
    return redirect('loginview')

@login_required(login_url='loginview')
def home(request):
    return render(request, 'index.html')

def medgrid4(request):
    return render(request,'med-grid-4.html')

def medgrid5(request):
    return render(request,'medicine-grid-5.html')



def medview(request):
    med_data = Item.objects.all()
    
    context ={'med_data':med_data}
    return render(request,'medview.html', context )

def medlist(request,id):
    category_data = Category.objects.get(id=int(id))
    ml_data = Item.objects.filter(category=category_data)

    paginator = Paginator(ml_data, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'med-grid-4.html', {'ml_data':ml_data, 'page_obj':page_obj})


def meddetail(request,id):
    mdetail_data = Item.objects.get(id=id)
    context = {'mdetail_data':mdetail_data}
    return render(request, 'detail.html',context)

def addproduct(request):
    form = MedicineModelForm()
    med_data = Item.objects.all()
    context = {'form':form,'med_data':med_data}
    if request.method =='POST':
        form1 =MedicineModelForm(request.POST,request.FILES)
        if form1.is_valid():
            form1.save()
            print('created new item')
            
        else:
            print('Error')
            return redirect('/')
    
    return render (request, 'addproduct.html',context)

def deleteitem(request,id):
    item_delete = Item.objects.filter(id=id)
    item_delete.delete()
    return redirect('/medicineview//')

def med_updateview(request,id):
    # pid = request.GET['pid']
    edit_data = Item.objects.get(id=id)
    
    
    form = MedicineModelForm(instance=edit_data)
    

    if request.method == 'POST':

        form = MedicineModelForm(request.POST, instance=edit_data)
        
        if form.is_valid():
            form.save()
        return redirect('/medicineview//')
    context = {'form': form}
    return render  (request,'addproduct.html',context)





def dis_view(request):
    dis_data = Disease.objects.all()
    context = {'dis_data':dis_data}
    return render(request,'disview.html', context)

def adddisease(request):
    form1 = DiseaseModelForm()
    context = {'form1':form1}

    if request.method =='POST':
        form1 =DiseaseModelForm(request.POST,request.FILES)
        if form1.is_valid():
            form1.save()
            print('created new item')
        else:
            print('Error')
        return redirect('/')
    
    return render (request, 'adddisease.html',context)

def deletedisease(request,id):
    disease_delete = Disease.objects.filter(id=id)
    disease_delete.delete()
    return redirect('/diseaseview/')

def dis_updateview(request,id):
    # pid = request.GET['pid']
    edit_data = Disease.objects.get(id=id)
    
    
    form1 = DiseaseModelForm(instance=edit_data)
    

    if request.method == 'POST':

        form1 = DiseaseModelForm(request.POST, instance=edit_data)
        
        if form1.is_valid():
            form1.save()
        return redirect('/diseaseview/')
    context = {'form1': form1}
    return render  (request,'adddisease.html',context)





# def addtocart(request,id):
#     item = Item.objects.get(id= id)
#     inv_no = request.session.get('invoice_no', None)
#     if inv_no:
#         cart_object = Cart.objects.get(id = inv_no)
#         item_exist=item.cartproduct_set.filter(item=item)
#         if item_exist.exists():
#             product_itm = item_exist.first()
#             product_itm.qty += 1
#             cart_object.total_amount += item.item_price
#             product_itm.save()
#             cart_object.total_amount += item.item_price 
#             cart_object.save()
            
#         else:
#             cp_obj = CartProduct.objects.create(cart= cart_object, item= item, qty= 1,price =item.item_price)
#             cart_object.total_amount += item.item_price 
#             cart_object.save()
#         print("in_no Have")
    
#     else:
#         cart_object = Cart.objects.create(total_amount=0)
#         request.session["invoice_no"] = cart_object.id
#         cp_obj = CartProduct.objects.create(cart= cart_object,item = item,qty= 1,price= item.item_price)
#         cart_object.total_amount += item.item_price 
#         cart_object.save()
        
#         print("in_no not Have")
#     return render(request, 'cart.html')
   




# def cartView(request):
#     inv_no = request.session.get('invoice_no', None)
#     if inv_no:
#         cart = Cart.objects.get(id=inv_no)
#         cart_products = CartProduct.objects.filter(cart=cart)
#         total = sum(items.price for items in cart_products)
#         cart.total_amount = total
#         cart.save()
#     else:
#         cart_products = []
#         total = 0

#     return render(request, 'cart.html', {
#         'cart_products': cart_products,
#         'total': total
#     })

# def increase_qty(request, id):
#     item = CartProduct.objects.get(id=id)
#     item.qty += 1
#     item.price = item.qty * item.item.item_price
#     item.save()
#     return redirect('/')


# def decrease_qty(request, id):
#     item = CartProduct.objects.get(id=id)
#     if item.qty > 1:
#         item.qty -= 1
#         item.price = item.qty * item.item.item_price
#         item.save()
#     else:
#         item.delete()  # Auto remove if qty hits 0
#     return redirect('/')



# def add_to_cart(request, item_id):
#     item = get_object_or_404(Item, id=item_id)

#     # Get or create cart (anonymous cart for now)
#     cart, created = Cart.objects.get_or_create(id=request.session.get('cart_id'), defaults={'created_date': timezone.now()})
#     request.session['cart_id'] = cart.id  # Store cart ID in session

#     # Check if item already exists in cart
#     cart_item, created = CartProduct.objects.get_or_create(cart=cart, item=item)
    
#     if not created:
#         cart_item.qty += 1
#         cart_item.price = cart_item.qty * item.item_price
#         cart_item.save()
#         cart.update_total_amount()
#     else:
#         cart_item.qty = 1
#         cart_item.price = item.item_price
#         cart_item.save()
    
#     return redirect('cart_list')  # Make sure this URL is defined

def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    cart_id = request.session.get('cart_id', None)
    
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
    else:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id

    cart_item, created = CartProduct.objects.get_or_create(
        cart=cart,
        item=item,
        defaults={'price': item.item_price, 'qty': 1}
    )

    if not created:
        cart_item.qty += 1
        cart_item.price = cart_item.qty * item.item_price
        cart_item.save()

    cart.update_total_amount()  

    return redirect('cart_list')




def cart_list(request):
    cart_id = request.session.get('cart_id')
    cart = get_object_or_404(Cart, id=cart_id)
    cart_items = CartProduct.objects.filter(cart=cart)

    total_amount = sum(item.price for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_amount': total_amount,
    }
    return render(request, 'cart.html', context)



def remove_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(CartProduct, id=cart_item_id)
    
    # Optional: check that the cart belongs to the user/session
    cart = cart_item.cart
    cart_item.delete()

    # Recalculate cart total
    cart.update_total_amount()

    return redirect('cart_list')  # 'cart' should be your URL name for the cart view


def checkoutview(request):
    cart_id = request.session.get('cart_id')
    cart = get_object_or_404(Cart, id=cart_id)
    cart_items = CartProduct.objects.filter(cart=cart)

    total_amount = sum(item.price for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_amount': total_amount,
    }
    return render(request,'checkout.html',context)