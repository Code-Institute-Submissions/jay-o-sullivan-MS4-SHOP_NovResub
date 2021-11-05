from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Js9PVI535AZS2oPzG5erK7LiwpZYNcLJaV4BxLzXQVVn3y9uQ4Od9FeT4oESwbfSBB0o01OG9JEGj9H3TCGVoHu00PqICWoxD',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)