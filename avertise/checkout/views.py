import stripe
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
from avertise.checkout.models import Order
from django.contrib.auth.decorators import login_required



# Initialize Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    # Get selected order type from query parameters
    order_type = request.GET.get('order_type')  # Example: 'logo', 'leaflet', 'poster'
    custom_description = request.GET.get('description', '')  # Custom description from user

    # Define fixed prices and descriptions for each order type
    order_data = {
        'logo': {'description': 'Logo Design', 'price': 50000},
        'leaflet': {'description': 'Leaflet Design', 'price': 20000},
        'poster': {'description': 'Poster Design', 'price': 30000},
    }

    # Handle invalid order_type
    if order_type not in order_data:
        return JsonResponse({'error': 'Invalid order type selected. Please choose a valid order type.'}, status=400)

    # Get the details for the selected order type
    order_details = order_data[order_type]

    # Create a payment intent with Stripe
    payment_intent = stripe.PaymentIntent.create(
        amount=order_details['price'],  # Stripe requires the amount in cents
        currency='usd',
        metadata={'order_type': order_type, 'custom_description': custom_description},  # Include custom description in metadata
    )

    # Pass data to the template
    context = {
        'order_description': custom_description if custom_description else order_details['description'],
        'order_price': order_details['price'] / 100,  # Convert cents to dollars for display
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
        'client_secret': payment_intent['client_secret'],  # Required for Stripe integration
    }

    
    # Your existing checkout logic...
    request.session['order_type'] = order_type
    request.session['description'] = custom_description if custom_description else order_details['description']
    request.session['price'] = order_details['price'] / 100  # Store in dollars
    
    # Render checkout.html...

    return render(request, 'checkout.html', context)


def success(request):
    # Retrieve order details from session or Stripe webhook data
    order_type = request.session.get('order_type')
    description = request.session.get('description')
    price = request.session.get('price')

    
    # print("Order Type:", request.session.get('order_type'))
    # print("Description:", request.session.get('description'))
    # print("Price:", request.session.get('price'))

    # Save the order to the database
    if request.user.is_authenticated and order_type and description and price:
        Order.objects.create(
            user=request.user,
            order_type=order_type,
            description=description,
            price=price,
        )

    # Clear session data after saving
    request.session.pop('order_type', None)
    request.session.pop('description', None)
    request.session.pop('price', None)


     # Pass data to the success.html template
    return render(request, 'success.html', {
        'message': 'Your payment was successful!',
        'order_type': order_type,
        'description': description,
        'price': price,
    })


# Profile view
@login_required
def profile(request):
    # Get all orders for the logged-in user
    user_orders = Order.objects.filter(user=request.user).order_by('-created_at')

    # Pass the orders to the profile.html template
    return render(request, 'profile.html', {'orders': user_orders})
