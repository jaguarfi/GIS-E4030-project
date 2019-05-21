from django.contrib.gis import admin
from .models import FloorLine


admin.site.register(FloorLine, admin.GeoModelAdmin)