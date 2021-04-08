from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.forms import inlineformset_factory
# Create your views here.
from .filters import *
from .forms import *

from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .restricters import unathenticated_user,allowed_users,admin_only
from django.contrib.auth.models import Group


# @allowed_users(allowed_roles=['admin'])
@admin_only
def dashboard(request):
    customer = Customer.objects.all()
    customer_filtered = CustomerFilter(request.GET,queryset=customer)
    customer = customer_filtered.qs
    context={
        'customers':customer,
        'title':'Dashboard',
        'filter':customer_filtered,
    }
    return render(request,'dashboard.html',context)


def customer(request):
    return render(request,'customer.html')


def customer_single(request,slug):
    customer = Customer.objects.get(slug=slug)
    orders = customer.order_set.all()
    order_filtered = OrderFilter(request.GET,queryset=orders)
    orders=order_filtered.qs
    context={
        'customer':customer,
        'title':'Customer Info',
        'orders':orders,
        'filter':order_filtered,
    }
    return render(request,'customer_single.html',context)



def side_html_file(request):
    customer_count = Customer.objects.all().count()
    product_count = Product.objects.all().count()
    order_count = Order.objects.all().count()
    context={
        'customer_count':customer_count,
        'product_count':product_count,
        'order_count':order_count,
    }

    return render(request,'side.html',context)


def product(request):
    return render(request,'product.html')




@login_required(login_url='login')
def CreateOrder(request):
    form = OrderForm()
    # form = OrderForm()
    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
        'form':form,
        'title':'Orders'
    }
    return render(request,'add_order.html',context)





def CreateOrder_specific(request,slug):
    Orderformset = inlineformset_factory(Customer,Order,fields=('product','status'))
    customer = Customer.objects.get(slug=slug)
    formset = Orderformset(instance=customer)
    # form = OrderForm()
    if request.method=='POST':
        formset = Orderformset(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context={
        'formset':formset,
        'title':'Orders'
    }
    return render(request,'add_order_specific.html',context)




def updateOrder(request,slug):
    order = Order.objects.get(slug=slug)
    form = OrderForm(instance=order)
    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
        'form':form,
        'title':'Orders'
    }
    return render(request,'update_order.html',context)


def deleteOrder(request,id):

    order = Order.objects.get(id=id)
    if request.method=='POST':
        order.delete()
        return redirect('/')
    context={
        'title':'Delete Order',
        'order':order,
    }
    return render(request,'delete_order.html',context)


@unathenticated_user
def RegisterUser(request):
    form = UserRegisterForm()
    if request.method=='POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request,'Successfully Registered')
            return redirect('login')
    context={
        'form':form,
        'title':'Register'
    }

    return render(request,'register.html',context)



@unathenticated_user
def LoginUser(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            nex_page = request.GET.get('next')
            return redirect(nex_page) if nex_page else redirect('/')
            
        else:
            messages.info(request,'Username or Password Incorrect')
    
    return render(request,'login.html',{})



def LogoutUser(request):
    logout(request)
    return redirect('/')



def UserPage(request):
    orders = request.user.customer.order_set.all()
    context={'orders':orders}
    return render(request,'user.html',context)


def Order_single_view(request,slug):
    order = Order.objects.get(slug=slug)
    context={'order':order}
    return render(request,'order_single.html',context)



def UserSettings(request):
    user = request.user.customer
    form = CustomerForm(instance=user)
    if request.method=='POST':
        form = CustomerForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('settings')
    context ={'form':form}
    return render(request,'settings.html',context)