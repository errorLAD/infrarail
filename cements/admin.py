from django.contrib import admin
from .models import Cement
from django.utils.html import format_html

# Register your models here.

class CementAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.cement_photo.url))

    thumbnail.short_description = 'MarbleCement Image'
    list_display = ('id','thumbnail','cement_title', 'city', 'color', 'model', 'year', 'body_style',  'is_featured')
    list_display_links = ('id', 'thumbnail', 'cement_title')
    list_editable = ('is_featured',)
    search_fields = ('id', 'cement_title', 'city', 'model', 'body_style')
    list_filter = ('city', 'model', 'body_style')
admin.site.register(Cement, CementAdmin)
# Register your models here.

