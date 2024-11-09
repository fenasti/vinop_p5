from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from wines.models import Wine

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, wine_id):
    """ Add a quantity of the specified wine to the shopping bag """

    wine = get_object_or_404(Wine, pk=wine_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if wine_id in list(bag.keys()):
        bag[wine_id] += quantity
        messages.success(request, f'Updated {wine.name} quantity to {bag[wine_id]}')
    else:
        bag[wine_id] = quantity
        messages.success(request, f'Added {wine.name} to your box')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)

def adjust_bag(request, wine_id):
    """Adjust the quantity of the specified wine to the specified amount"""

    wine = get_object_or_404(Wine, pk=wine_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[wine_id] = quantity
        messages.success(request, f'Updated {wine.name} quantity to {bag[wine_id]}')
    else:
        bag.pop(wine_id, None)
        messages.success(request, f'Removed {wine.name} from your box')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, wine_id):
    """Remove the specified wine from the shopping bag"""

    wine = get_object_or_404(Wine, pk=wine_id)

    try:
        bag = request.session.get('bag', {})
        bag.pop(wine_id, None)
        messages.success(request, f'Removed {wine.name} from your box')
        
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)