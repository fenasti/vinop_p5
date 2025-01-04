from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Wine
from reviews.models import Review
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
    """ A view to show wine details and reviews """

    wine = get_object_or_404(Wine, pk=wine_id)
    reviews = Review.objects.filter(wine=wine).order_by('-created_at')  # Fetch reviews for this wine

    context = {
        'wine': wine,
        'reviews': reviews,  # Add the reviews to the context
    }

    return render(request, 'wines/wine_detail.html', context)

@login_required
def add_wine(request):
    """ Add a wine to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = WineForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added wine!')
            return redirect(reverse('add_wine'))
        else:
            messages.error(request, 'Failed to add wine. Please ensure the form is valid.')
    else:
        form = WineForm()
        
    template = 'wines/add_wine.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_wine(request, wine_id):
    """ Edit a wine in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    wine = get_object_or_404(Wine, pk=wine_id)
    if request.method == 'POST':
        form = WineForm(request.POST, request.FILES, instance=wine)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated wine!')
            return redirect(reverse('wine_detail', args=[wine.id]))
        else:
            messages.error(request, 'Failed to update wine. Please ensure the form is valid.')
    else:
        form = WineForm(instance=wine)
        messages.info(request, f'You are editing {wine.name}')

    template = 'wines/edit_wine.html'
    context = {
        'form': form,
        'wine': wine,
    }

    return render(request, template, context)

@login_required
def delete_wine(request, wine_id):
    """ Delete a wine from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    wine = get_object_or_404(Wine, pk=wine_id)
    wine.delete()
    messages.success(request, 'Wine deleted!')
    return redirect(reverse('wines'))