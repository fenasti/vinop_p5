from django.shortcuts import render
from subscriptions.forms import SubscriptionForm

# Create your views here.

def index(request):
    """ A view to return the index page """
    form = SubscriptionForm()  # Initialize the subscription form

    return render(request, 'home/index.html', {'form': form})