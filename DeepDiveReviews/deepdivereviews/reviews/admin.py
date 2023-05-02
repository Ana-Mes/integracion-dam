from django.contrib import admin
from .models import DivingSpot

# Register your models here.
class DivingSpotAdmin(admin.ModelAdmin):
    list_display = ('created', 'name')
    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }

admin.site.register(DivingSpot, DivingSpotAdmin)