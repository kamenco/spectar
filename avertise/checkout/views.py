import stripe
from django.shortcuts import render, redirect
from django.conf import settings

# Create your views here.


# Load Stripe API keys from settings
stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    if request.method == 'POST':
        # Simulate payment processing for now
        try:
            # Create a Stripe payment intent
            intent = stripe.PaymentIntent.create(
                amount=1000,  # Amount in cents (e.g., $10.00)
                currency='usd',
                payment_method_types=['card']
            )
            return render(request, 'checkout/checkout.html', {
                'client_secret': intent.client_secret
            })
        except Exception as e:
            return render(request, 'checkout/checkout.html', {'error': str(e)})

    return render(request, 'checkout/checkout.html')

def success(request):
    return render(request, 'checkout/success.html')

