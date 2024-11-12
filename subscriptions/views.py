from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SubscriptionForm
from .models import Subscription


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save()
            _send_subscription_confirmation_email(subscription)
            messages.success(request, 'Thank you for subscribing!')
            return redirect('home')
    # else:
    #     form = SubscriptionForm()
    # return render(request, 'subscriptions/subscribe_success.html', {'form': form})


def _send_subscription_confirmation_email(subscription):
    """Send the subscriber a confirmation email."""
    cust_email = subscription.email
    subject = render_to_string(
        'subscriptions/confirmation_emails/subscription_email_subject.txt'
    )
    body = render_to_string(
        'subscriptions/confirmation_emails/subscription_email_body.txt',
        {'contact_email': settings.DEFAULT_FROM_EMAIL}
    )

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email],
        fail_silently=False,
    )