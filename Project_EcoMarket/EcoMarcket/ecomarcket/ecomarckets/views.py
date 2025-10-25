from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product
from .forms import LoginForm, RegisterForm

# Create your views here.
def home(req):
    products = Product.objects.all()
    context = {'products': products}
    return render(req, 'ecomarckets/home.html', context)

def login_view(req):
    if req.method == 'POST':
        login_form = LoginForm(req.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(req, username=username, password=password)
            if user is not None:
                login(req, user)
                messages.success(req, 'Login successful!')
                return redirect('home')
            else:
                messages.error(req, 'Invalid username or password!')
    else:
        login_form = LoginForm()
    
    return render(req, 'ecomarckets/login.html', {'form': login_form})

def register_view(req):
    if req.method == 'POST':
        register_form = RegisterForm(req.POST)
        if register_form.is_valid():
            user = register_form.save()
            username = register_form.cleaned_data.get('username')
            messages.success(req, f'Account created successfully for {username}!')
            return redirect('login')
    else:
        register_form = RegisterForm()
    
    return render(req, 'ecomarckets/register.html', {'form': register_form})

@login_required
def logout_view(req):
    logout(req)
    messages.success(req, 'Logout successful!')
    return redirect('home')