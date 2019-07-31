from django.contrib import admin
from .models import Contact
from django.contrib import admin

class ContactsAdmin(admin.ModelAdmin):
    list_display=('name', 'phone', 'email')

admin.site.register(Contact, ContactsAdmin)
