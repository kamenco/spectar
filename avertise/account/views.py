# account/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'account/account_signup.html', {'form': form})

# Profile view

@login_required
def profile(request):
    orders = request.user.orders.all()  # Fetch all orders for the logged-in user
    return render(request, 'profile.html', {'orders': orders})
