from django.shortcuts import render, redirect
from django.contrib import messages 
from django.shortcuts import render


def profile(request):
    user = request.user
    customer = request.user.customerinfo
    
    if request.method == 'POST':
        customer.phone_number = request.POST.get('phone', '')
        customer.address = request.POST.get('address', '')
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        customer.save()
        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')

    return render(request, 'customer/profile.html')

