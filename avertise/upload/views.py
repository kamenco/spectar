from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import CompletedWork
from .forms import CompletedWorkForm
from checkout.models import Order

# Create your views here.

@user_passes_test(lambda u: u.is_superuser)
def upload_completed_work(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    completed_work, created = CompletedWork.objects.get_or_create(order=order)
    if request.method == 'POST':
        form = CompletedWorkForm(request.POST, request.FILES, instance=completed_work)
        if form.is_valid():
            form.save()
            # Redirect to the user's profile page after successful upload
            return redirect('account:profile')  # Ensure this namespace matches your URLs
    else:
        form = CompletedWorkForm(instance=completed_work)
    return render(request, 'upload/upload_completed_work.html', {'form': form, 'order': order})


@user_passes_test(lambda u: u.is_superuser)
def view_all_orders(request):
    orders = Order.objects.all()  # Fetch all orders from the database
    return render(request, 'upload/all_orders.html', {'orders': orders})