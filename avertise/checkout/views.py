import logging
import stripe
from django.shortcuts import render, redirect
from django.conf import settings  # To access STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY
from django.http import JsonResponse


logger = logging.getLogger(__name__)

# Initialize Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    # Get selected order type from query parameters
    order_type = request.GET.get('order_type')  # Example: 'logo', 'leaflet', 'poster'
    logger.info(f"Received order_type: {order_type}")

    # Define fixed prices and descriptions for each order type
    order_data = {
        'logo': {'description': 'Logo Design', 'price': 50000},
        'leaflet': {'description': 'Leaflet Design', 'price': 20000},
        'poster': {'description': 'Poster Design', 'price': 30000},
    }

# Handle invalid order_type
    if order_type not in order_data:
        logger.error(f"Invalid order_type: {order_type}")
        return JsonResponse({'error': 'Invalid order type selected. Please choose a valid order type.'}, status=400)

    # Get the details for the selected order type (default to an empty dict if not found)
    order_details = order_data.get(order_type, {'description': 'Unknown', 'price': 0})
    logger.info(f"Order details: {order_details}")

     # Check if the amount is above Stripe's minimum threshold
    if order_details['price'] < 50:  # Assuming the minimum is $0.50 (50 cents)
        return JsonResponse({'error': 'The amount is too low to process this transaction.'}, status=400)

    # Create a payment intent with Stripe
    payment_intent = stripe.PaymentIntent.create(
        amount=int(order_details['price'] * 100),  # Stripe requires the amount in cents
        currency='usd',
        metadata={'order_type': order_type},  # You can pass order details as metadata
    )

    # Pass data to the template
    context = {
        'order_description': order_details['description'],
        'order_price': order_details['price'] / 100,  # Convert cents to dollars for display
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
        'client_secret': payment_intent['client_secret'],  # Required for Stripe integration
    }

    return render(request, 'checkout.html', context)


def success(request):
    return render(request, 'success.html', {'message': 'Your payment was successful!'})