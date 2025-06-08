from django.shortcuts import render, redirect, HttpResponse
from ourapp.models import *
from django.contrib.auth.models import User
from .models import *
from django.core.paginator import Paginator
from .form import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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
