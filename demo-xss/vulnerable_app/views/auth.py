from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth import logout, authenticate, login
from django.views.defaults import page_not_found
from django.db import transaction
from vulnerable_app.models import User, CustomerInfo


def customer_login(request):
    if request.method == "GET":
        return render(request, 'customer/login.html')
    elif request.method == "POST":
        email = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Welcome back, {user.email}!')
            return redirect('home')
        messages.error(request, 'Invalid email or password')
        return render(request, 'customer/login.html')
    else:
        return page_not_found(request, exception=None)


def customer_register(request):
    if request.method == "GET":
        return render(request, 'customer/register.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
        # elif len(password1) < :
        #     messages.error(request, 'Password must be at least 8 characters')
        else:
            with transaction.atomic():
                user = User.objects.create_user(
                    username=email,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=password1
                )
                CustomerInfo.objects.create(
                    user=user,
                    phone_number=phone
                )
                login(request, user)  # Auto-login
                messages.success(request, f'Welcome to MusicMart, {user.first_name}!')
                return redirect('home')
        return render(request, 'customer/register.html')
    else:
        return page_not_found(request, exception=None)

def logout_view(request):
    logout(request) 
    messages.success(request, 'You have been logged out successfully!')
    return redirect('home')


