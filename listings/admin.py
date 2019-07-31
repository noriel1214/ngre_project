from django.contrib import admin
from .models import Listing

class ListingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','address', 'city','state', 'zipcode','is_published','realtor')
    list_editable = ('title','address','city','state', 'zipcode','is_published','realtor')

admin.site.register(Listing, ListingsAdmin)