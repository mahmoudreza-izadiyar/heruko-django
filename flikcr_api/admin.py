from django.contrib import admin
from .models import Preset, FavouritePlaces


class PresetAdmin(admin.ModelAdmin):
    fields = ['locationName', 'latitude', 'longitude']

    
admin.site.register(Preset, PresetAdmin)


class FavouritePlacesAdmin(admin.ModelAdmin):
    fields = ['locationName', 'latitude', 'longitude']


admin.site.register(FavouritePlaces, FavouritePlacesAdmin)
