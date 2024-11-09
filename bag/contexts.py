from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from wines.models import Wine

def bag_contents(request):

    bag_items = []
    total = 0
    wine_count = 0
    bag = request.session.get('bag', {})

    for wine_id, quantity in bag.items():
        wine = get_object_or_404(Wine, pk=wine_id)
        total += quantity * wine.price
        wine_count += quantity
        bag_items.append({
            'wine_id': wine_id,
            'quantity': quantity,
            'wine': str(wine),      #render wine as a string instead of an object.
        })
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'wine_count': wine_count,
    }

    return context