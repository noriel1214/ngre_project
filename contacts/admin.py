from django.contrib import admin
from .models import Contact
from django.contrib import admin

class ContactsAdmin(admin.ModelAdmin):
    list_display=('listing_id', 'address', 'name', 'email', 'phone')

admin.site.register(Contact, ContactsAdmin)
