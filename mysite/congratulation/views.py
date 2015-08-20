from congratulation.forms import DetailsForm, CustomerForm
from congratulation.models import Customer, Details
from datetime import datetime
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.template import Context

def index(request):
    customer_list = Customer.objects.order_by('-last_name')[:25]
    context = {'username':auth.get_user(request).username, 'customer_list': customer_list}
    return render(request, 'congratulation/index.html', context)

def detail(request):
    current_user = request.user
    try:
        c = Customer.objects.get(user_id = current_user.id)
        customer = get_object_or_404(Customer, pk=c.id)
        orders_list = Details.objects.filter(customer_id=c.id)
        context = {'username':auth.get_user(request).username, 'orders_list': orders_list, 'customer': customer}
        return render(request, 'congratulation/detail.html', context)
    except ObjectDoesNotExist:
        return redirect ('/congratulation/information')

def join(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request,newuser)
            return redirect('/congratulation/information', {'id':newuser.id})
        else:
            args['form'] = newuser_form
    return render_to_response('congratulation/join.html', args)

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/congratulation/')
        else:
            args['login_error'] = "User is not found"
            return render_to_response('congratulation/login.html', args)
    else:
        return render_to_response('congratulation/login.html', args)

def logout(request):
    auth.logout(request)
    return redirect("/congratulation/")

def information(request):
    current_user = request.user
    try:
        customer = Customer.objects.get(user_id = current_user.id)
        if request.method == 'POST':
            form = CustomerForm(request.POST)
            if form.is_valid():
                form = CustomerForm(request.POST, instance=customer)
                form.save()
                return redirect('/congratulation/detail')
        else:
            form = CustomerForm(instance=customer)
        return render(request, 'congratulation/add_customer.html', {'username':auth.get_user(request).username, 'form': form})
    except ObjectDoesNotExist:
        if request.method == 'POST':
            form = CustomerForm(request.POST)
            if form.is_valid():
                o = Customer.objects.create(user_id = current_user.id)
                form = CustomerForm(request.POST, instance=o)
                form.save()
                return redirect('/congratulation/detail')
        else:
            form = CustomerForm()
        return render(request, 'congratulation/add_customer.html', {'username':auth.get_user(request).username, 'form': form})

def add_customer(request):
    return render(request, 'congratulation/add_customer.html')

def delete_account(request):
    current_user = request.user
    c = Customer.objects.get(user_id = current_user.id)
    orders_list = Details.objects.filter(customer_id=c.id)
    if orders_list != None:
        for order in orders_list:
            order.delete()
    c.delete()
    current_user.delete()
    return redirect('/congratulation/')

def order(request):
    current_user = request.user
    c = Customer.objects.get(user_id = current_user.id)
    if request.method == 'POST':
        form = DetailsForm(request.POST)
        if form.is_valid():
            a = Details.objects.create(customer_id=c.id, date=datetime.now())
            form = DetailsForm(request.POST, instance=a)
            form.save()
            return HttpResponseRedirect('/congratulation/detail')
    else:
        form = DetailsForm()
    return render(request, 'congratulation/add_order.html', {'username':auth.get_user(request).username, 'form': form, 'id':c.id})

def add_order(request, customer_id):
    return render(request, 'congratulation/add_order.html', {'id':customer_id})

def edit_order(request, details_id):
    order = Details.objects.get(pk=details_id)
    if request.method == 'POST':
        form = DetailsForm(request.POST)
        if form.is_valid():
            form = DetailsForm(request.POST, instance=order)
            form.save()
            return redirect('congratulation:congr', details_id )
    else:
        form = DetailsForm(instance=order)
    return render(request, 'congratulation/edit_order.html', {'username':auth.get_user(request).username, 'form': form, 'id':details_id})

def delete_order(request, details_id):
    d = Details.objects.get(pk=details_id)
    d.delete()
    return redirect('/congratulation/detail')

def confirmation(request):
    return render(request, 'congratulation/confirmation.html', {'username':auth.get_user(request).username})

def congr(request, details_id):
    order = get_object_or_404(Details, pk=details_id)
    return render(request, 'congratulation/congr.html', {'username':auth.get_user(request).username, 'order': order})