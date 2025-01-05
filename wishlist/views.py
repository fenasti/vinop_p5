from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Wishlist
from wines.models import Wine

@login_required
def wishlist_detail(request):
    wishlist = request.user.wishlist
    return render(request, 'wishlist/wishlist_detail.html', {'wishlist': wishlist})

@login_required
def add_to_wishlist(request, wine_id):
    wishlist = request.user.wishlist
    wine = get_object_or_404(Wine, id=wine_id)
    wishlist.wines.add(wine)
    return redirect('wishlist_detail')

@login_required
def remove_from_wishlist(request, wine_id):
    wishlist = request.user.wishlist
    wine = get_object_or_404(Wine, id=wine_id)
    wishlist.wines.remove(wine)
    return redirect('wishlist_detail')