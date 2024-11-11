from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Wine
from .forms import WineForm

# Create your views here.

def all_wines(request):
    """ A view to show all wines, including sorting and search queries """

    wines = Wine.objects.all()
    query = None
    grape_type = None
    current_country = None

    if request.GET:
        if 'grape' in request.GET:
            grape_type = request.GET['grape'].replace('_', ' ')
            wines = wines.filter(grapes__iexact=grape_type)

        if 'country' in request.GET:
            current_country = request.GET['country'].replace('_', ' ')
            wines = wines.filter(country__iexact=current_country) # __iexact means case insesitive

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('wines'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            wines = wines.filter(queries)

    context = {
        'wines': wines,
        'search_term': query,
        'selected_grape': grape_type,
        'selected_country' : current_country,
    }

    return render(request, 'wines/wines.html', context)

def wine_detail(request, wine_id):
    """ A view to show wines details """

    wine = get_object_or_404(Wine, pk=wine_id)

    context = {
        'wine': wine,
    }

    return render(request, 'wines/wine_detail.html', context)

def add_wine(request):
    """ Add a wine to the store """
    form = WineForm()
    template = 'products/add_wine.html'
    context = {
        'form': form,
    }

    return render(request, template, context)