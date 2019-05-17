import os
from django.contrib.gis.utils import LayerMapping
from .models import FloorLine



app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))


'''
Provides a function to read data from a .shp file to the PostGIS database.
How to use for the given data in bash:
>py manage.py shell
>from mapapp import load
>load.read_lines('buildings_3851.shp', 'EPSG_building')
These commands should work by copy&paste in the terminal. if more data is added later, simply replace file&folder name variables as needed.

The function rename_buildings taking in arguments of old and new building name and will replace the name of all FloorLine objects that belond to a building
with the old name. So for renaming a building.
'''

def read_lines(file, folder):
    #reads floorlines of one floor from a .shp. Input params are filename and foldername
    inputshp = os.path.join(app_path, folder, file) 
    floor_mapper = {'linja' : 'LINESTRING', 'level' : 'level', 'building_name' : 'name', 'layer' : 'Layer'}
    lines = LayerMapping(FloorLine, inputshp, floor_mapper, transform=True)
    lines.save(strict=False, verbose=True)


def rename_building(old_name, new_name):
    building = FloorLine.objects.filter(building_name=old_name)
    for line in building:
        line.building_name = new_name
        line.save()


