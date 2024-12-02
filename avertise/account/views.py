# account/views.py
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from checkout.models import Order

# Signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('account:profile')  # Redirect to profile after signup
    else:
        form = UserCreationForm()
    return render(request, 'account/account-signup.html', {'form': form})

# Profile view

# @login_required
# def profile(request):
   # orders = request.user.orders.all()  # Fetch all orders for the logged-in user
   # return render(request, 'account/profile.html')


@login_required
def profile(request):
    # Fetch all orders for the logged-in user and include related completed work
    orders = Order.objects.filter(user=request.user).select_related('completed_work')
    return render(request, 'account/profile.html', {'orders': orders})

