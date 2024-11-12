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
            # Save the subscription and send the confirmation email
            subscription = form.save()
            _send_subscription_confirmation_email(subscription)
            
            # Success message and redirect to subscription success page
            messages.success(request, 'Thank you for subscribing!')
            return redirect('subscribe_success')  # Redirect to the subscription success page
        else:
            # If form is invalid, show error messages and render the same page (index.html)
            messages.error(request, 'There was an issue with your subscription. Please try again.')
            return redirect('home')  # Redirect back to the homepage or form page
    else:
        form = SubscriptionForm()

    return render(request, 'index.html', {'form': form})  # Render to index page with form


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

def subscription_success(request):
    # Render the success page with the subscription data
    return render(request, 'subscriptions/subscribe_success.html')