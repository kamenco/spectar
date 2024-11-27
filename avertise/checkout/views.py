import stripe
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse

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

    return render(request, 'checkout.html', context)


def success(request):
    return render(request, 'success.html', {'message': 'Your payment was successful!'})
