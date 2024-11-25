from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import GraphicOrder

# Home view for orders (e.g., to show the order form)
def order_home(request):
    return render(request, 'order/order.html')

# Submit an order (requires login)
@login_required
def submit_order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        order_type = request.POST.get('order_type')
        comments = request.POST.get('comments')

        try:
            # Save the order in the database
            GraphicOrder.objects.create(
                user=request.user,  # Now this will always be a logged-in user
                type=order_type,
                size="Custom",  # Placeholder if size is not collected
                description=comments,
                quote=0.0,  # Replace with logic to calculate a quote
            )
            return redirect('redirect_to_checkout')
        except Exception as e:
            messages.error(request, f"Error while submitting order: {str(e)}")
            return render(request, 'order/order.html')
    return render(request, 'order/order.html')

# Redirect to the checkout page (assuming a checkout view exists)
def redirect_to_checkout(request):
    return redirect('checkout')  # Replace 'checkout' with the correct URL name if different
