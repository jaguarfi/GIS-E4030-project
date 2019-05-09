from django.contrib.gis import admin
from .models import WorldBorder, FloorLine

admin.site.register(WorldBorder, admin.GeoModelAdmin)
#admin.site.register(Floor, admin.GeoModelAdmin)
admin.site.register(FloorLine, admin.GeoModelAdmin)