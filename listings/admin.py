from django.contrib import admin
from .models import Listing

class ListingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','city','state', 'zipcode', 'price','is_published','realtor')
    list_editable = ('title','city','state', 'zipcode', 'price','is_published','realtor')

admin.site.register(Listing, ListingsAdmin)