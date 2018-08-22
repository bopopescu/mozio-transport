from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin

from area.models import Area


admin.site.register(Area, LeafletGeoAdmin)
