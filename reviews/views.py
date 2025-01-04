from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .forms import ReviewForm
from wines.models import Wine
from django.contrib.auth.decorators import login_required

@login_required
def add_review(request, wine_id):
    wine = get_object_or_404(Wine, id=wine_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.wine = wine
            review.save()
            return redirect('wine_detail', wine_id=wine.id)
    else:
        form = ReviewForm()
    return render(request, 'reviews/add_review.html', {'form': form, 'wine': wine})