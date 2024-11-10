from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your box at the moment")
        return redirect(reverse('wines'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QF01jBsGtbqr4E89jQ9ejaZQARiLjTvWeyPSv6jBgkLaXGM8mPwBevImCM8WZ4URSAhKosfTNjTKkf9Daoee3Dr00YsWt7I7x',
        'client_secret': 'sk_test_51QF01jBsGtbqr4E84UHWwwXBjyz0U36RxS3iqLWJyvAWBE5lRcufiBL9cXzFSOIUoTD069ljhWlzJcKEtc7hMWW800RT27IEck',
    }

    return render(request, template, context)