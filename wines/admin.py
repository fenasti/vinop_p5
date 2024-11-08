from django.contrib import admin
from .models import Wine

# Register your models here.

class WineAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'grapes',
        'country',
        'picture',
    )

admin.site.register(Wine, WineAdmin)