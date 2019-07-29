from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'is_mvp')
    list_editable = ('name', 'phone', 'email', 'is_mvp')

admin.site.register(Realtor, RealtorAdmin)
