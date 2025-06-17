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
from django.views.decorators.http import require_POST
from .models import Customer
from django.contrib.auth.models import User

# Create your views here.
def homeview(request):
    return render(request,'index.html')



from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Customer

from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Customer

def customer_register(request):
    # ✅ Login ဝင်ပြီးသားဆိုရင် Customer profile ရှိလားစစ်မယ်
    if request.user.is_authenticated:
        try:
            request.user.customer  # မရှိရင် DoesNotExist error တက်မယ်
            messages.warning(request, "Customer profile ရှိပြီးသား ဖြစ်နေပါတယ်။")
            return redirect('homeview')  # သင့်ရဲ့ main/home page ကို redirect လုပ်
        except Customer.DoesNotExist:
            pass  # Profile မရှိသေးလို့ register form ကိုပြပေးမယ်

    if request.method == 'POST':
        data = request.POST
        username = data.get('customer[username]')
        password = data.get('customer[password]')
        confirm = data.get('customer[confirm_password]')
        email = data.get('customer[email]')
        first_name = data.get('customer[first_name]')
        last_name = data.get('customer[last_name]')
        phone = data.get('customer[phno]')

        # ✅ Password check
        if password != confirm:
            messages.error(request, "Passwords do not match.")
            return redirect('customer_register')

        # ✅ Duplicate username check
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('customer_register')

        # ✅ Create user
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )

        # ✅ Login after registration
        login(request, user)

        # ✅ Create related Customer profile
        Customer.objects.create(
            user=user,
            phone=phone,
            address=''  # Or get address from form if you have it
        )

        messages.success(request, "Account created and logged in successfully.")

        # ✅ Next redirect logic
        next_url = request.GET.get('next')
        if next_url:
            return redirect(next_url)

        return redirect('cart_list')  # Default redirect

    return render(request, 'register.html')
    

   
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
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
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

def addsupplier(request):
    form2 = CompanyModelForm()
    sup_data = Supplier.objects.all()
    context = {'form2':form2,'sup_data':sup_data}
    if request.method =='POST':
        form2 =CompanyModelForm(request.POST,request.FILES)
        if form2.is_valid():
            form2.save()
            print('created new item')
            
        else:
            print('Error')
            return redirect('/')
    
    return render (request, 'addcompany.html',context)

def companyview(request):
    com_data = Supplier.objects.all()
    
    context ={'com_data':com_data}
    return render(request,'companyview.html', context )
def supvounchar(request):
    supvounchar_data = Item.objects.all()
    
    context ={'supvounchar_data':supvounchar_data}
    return render(request,'supvounchar.html', context )



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







  
   

# def cart_list(request):
#     cart_id = request.session.get('cart_id')
#     cart = get_object_or_404(Cart, id=cart_id)
#     cart_items = CartProduct.objects.filter(cart=cart)

#     total_amount = sum(item.price for item in cart_items)

#     context = {
#         'cart_items': cart_items,
#         'total_amount': total_amount,
#     }
#     return render(request, 'cart.html', context)

















# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# from .models import CartProduct

# @csrf_exempt  # Use @login_required + csrf_protect in production
# def update_qty(request):
#     if request.method == 'POST':
#         item_id = request.POST.get('id')
#         action = request.POST.get('action')

#         if not request.user.is_authenticated:
#             return JsonResponse({'error': 'Authentication required'}, status=401)

#         try:
#             cart_item = CartProduct.objects.get(id=item_id, user=request.user)

#             if action == 'increase':
#                 cart_item.qty += 1
#             elif action == 'decrease' and cart_item.qty > 1:
#                 cart_item.qty -= 1
#             cart_item.save()

#             subtotal = cart_item.qty * cart_item.price

#             # Get updated total cart amount for this user
#             cart_items = CartProduct.objects.filter(user=request.user)
#             total_amount = sum(item.qty * item.price for item in cart_items)

#             return JsonResponse({
#                 'qty': cart_item.qty,
#                 'subtotal': subtotal,
#                 'total_amount': total_amount
#             })

#         except CartItem.DoesNotExist:
#             return JsonResponse({'error': 'Item not found'}, status=404)

#     return JsonResponse({'error': 'Invalid request'}, status=400)
# views.py




from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    user = request.user

    cart, created = Cart.objects.get_or_create(user=user)

    cart_product, created = CartProduct.objects.get_or_create(
        cart=cart,
        item=item,
        defaults={'qty': 1, 'price': item.item_price}
    )

    if not created:
        cart_product.qty += 1
        cart_product.price = item.item_price * cart_product.qty
        cart_product.save()

    cart.update_total_amount()

    return redirect('medview')

# views.py



@login_required
def cart_list(request):
    user = request.user
    try:
        cart = Cart.objects.get(user=user)
        cart_items = CartProduct.objects.filter(cart=cart)
        total = sum([cp.qty * cp.item.item_price for cp in cart_items])
    except Cart.DoesNotExist:
        cart_items = []
        total = 0

    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'cart_list.html', context)


def increase_quantity(request, item_id):
    cart = request.session.get('cart', {})
    if str(item_id) in cart:
        cart[str(item_id)]['quantity'] += 1
    request.session['cart'] = cart
    return redirect('cart_list')

def decrease_quantity(request, item_id):
    cart = request.session.get('cart', {})
    if str(item_id) in cart:
        cart[str(item_id)]['quantity'] -= 1
        if cart[str(item_id)]['quantity'] <= 0:
            del cart[str(item_id)]
    request.session['cart'] = cart
    return redirect('cart_list')

def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    if str(item_id) in cart:
        del cart[str(item_id)]
    request.session['cart'] = cart
    return redirect('cart_list')



from django.contrib.auth.decorators import user_passes_test

def is_customer(user):
    return hasattr(user, 'customer')  # user မှာ customer profile ရှိမရှိစစ်တာ

@login_required
@user_passes_test(is_customer)
def customer_dashboard(request):
    orders = Sale.objects.filter(user=request.user)  # or related customer
    return render(request, 'customer/dashboard.html', {'orders': orders})

@login_required
@user_passes_test(is_customer)
def customer_invoice_detail(request, invoice_no):
    sale = get_object_or_404(Sale, invoice_no=invoice_no, user=request.user)
    sale_items = SaleItem.objects.filter(sale=sale)
    return render(request, 'customer/invoice_detail.html', {
        'sale': sale,
        'sale_items': sale_items,
    })




# def sales_report(request):
#     today = now().date()

#     # Daily sales
#     daily_sales = Sale.objects.filter(date__date=today)
#     daily_total = daily_sales.aggregate(Sum('total_amount'))['total_amount__sum'] or 0

#     # Monthly sales
#     monthly_sales = Sale.objects.filter(date__year=today.year, date__month=today.month)
#     monthly_total = monthly_sales.aggregate(Sum('total_amount'))['total_amount__sum'] or 0

#     # Yearly sales
#     yearly_sales = Sale.objects.filter(date__year=today.year)
#     yearly_total = yearly_sales.aggregate(Sum('total_amount'))['total_amount__sum'] or 0

#     context = {
#         'daily_sales': daily_sales,
#         'daily_total': daily_total,
#         'monthly_total': monthly_total,
#         'yearly_total': yearly_total,
#     }
#     return render(request, 'sales-report.html', context)






from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Cart, CartProduct, Sale, SaleItem, Customer

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils import timezone


from django.contrib import messages

@login_required
def checkout(request):
    user = request.user

    # ✅ Check if customer profile exists
    if not hasattr(user, 'customer'):
        messages.warning(request, "Checkout မလုပ်နိုင်ပါ။ Customer profile မရှိသေးပါ။")
        return redirect('customer_register')  # or show a form to create profile

    try:
        cart = Cart.objects.get(user=user)
        cart_items = CartProduct.objects.filter(cart=cart)

        if not cart_items.exists():
            messages.warning(request, "Your cart is empty.")
            return redirect('cart_list')

        sale = Sale.objects.create(
            invoice_no=f"INV-{timezone.now().strftime('%Y%m%d%H%M%S')}",
            user=user,
            customer=user.customer,
            total_amount=cart.total_amount
        )

        for cp in cart_items:
            SaleItem.objects.create(
                sale=sale,
                item=cp.item,
                quantity=cp.qty,
                price=cp.price
            )
            cp.item.item_quatity -= cp.qty
            cp.item.save()

        cart_items.delete()
        cart.total_amount = 0
        cart.save()

        messages.success(request, "Checkout completed successfully.")
        return render(request,'checkout.html', {'sale': sale})

    except Cart.DoesNotExist:
        messages.error(request, "Cart not found.")
        return redirect('cart_list')

from django.utils.timezone import now
from django.db.models import Sum
import datetime

def daily_sales_report(request):
    today = now().date()
    sales = Sale.objects.filter(date__date=today)
    total = sales.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    return render(request, 'reports/daily.html', {'sales': sales, 'total': total, 'today': today})

def monthly_sales_report(request):
    today = now().date()
    sales = Sale.objects.filter(date__year=today.year, date__month=today.month)
    total = sales.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    return render(request, 'reports/monthly.html', {'sales': sales, 'total': total,'today': today})

def yearly_sales_report(request):
    today = now().date()
    sales = Sale.objects.filter(date__year=today.year)
    total = sales.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    return render(request, 'reports/yearly.html', {'sales': sales, 'total': total, 'today': today})
