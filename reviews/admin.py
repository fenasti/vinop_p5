from django.contrib import admin
from .models import Review

# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'wine',
        'rating',
        'comment',
        'created_at',
    )
    list_filter = ('rating', 'created_at')
    search_fields = ('user__username', 'wine__name', 'comment')

admin.site.register(Review, ReviewAdmin)