from django.contrib import admin
from .models import Contactcement

# Register your models here.
class ContactCementAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'cement_title', 'city', 'create_date')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email', 'cement_title')
    list_per_page = 25

admin.site.register(Contactcement, ContactCementAdmin)
