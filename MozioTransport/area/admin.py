from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
from area.models import Area

admin.site.register(Area, LeafletGeoAdmin)