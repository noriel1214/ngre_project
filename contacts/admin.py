from django.contrib import admin
from .models import Contact
from django.contrib import admin

class ContactsAdmin(admin.ModelAdmin):
    list_display=('firstname', 'lastname', 'phone', 'email')

admin.site.register(Contact, ContactsAdmin)
