from django.shortcuts import render, redirect
from .models import GraphicOrder


# Create your views here.


def submit_order(request):
    if request.method == 'POST':
        name = request.POST['name']
        order_type = request.POST['order_type']
        comments = request.POST['comments']
        # Save the order in the database
        GraphicOrder.objects.create(
            user=request.user,  # Assuming the user is logged in
            type=order_type,
            size="Custom",  # Placeholder if size is not collected
            description=comments,
            quote=0.0,  # Replace with logic to calculate a quote
        )
        return redirect('home')  # Redirect after successful submission
    return render(request, 'order.html')

def order_home(request):
    return render(request, 'order/order.html')  # Path to your order.html