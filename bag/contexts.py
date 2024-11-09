from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from wines.models import Wine

def bag_contents(request):

    bag_items = []
    total = 0
    wine_count = 0
    bag = request.session.get('bag', {})

    for wine_id, item_data in bag.items():
        if isinstance(item_data, int):  
            wine = get_object_or_404(Wine, pk=wine_id)
            total += item_data * wine.price
            wine_count += item_data
            bag_items.append({
                'wine_id': wine_id,
                'quantity': item_data,
                'wine': wine,
            })
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'wine_count': wine_count,
    }

    return context