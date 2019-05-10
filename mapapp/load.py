import os
from django.contrib.gis.utils import LayerMapping
from .models import FloorLine



app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))
#floor_mapper = {'geometry' : 'MULTILINESTRING'}
#floor_mapper = {'linja' : 'LINESTRING'}

def read_lines(file, folder):
    #reads floorlines of one floor from a .shp. Input params are filename and foldername
    inputshp = os.path.join(app_path, folder, file) 
    floor_mapper = {'linja' : 'LINESTRING', 'level' : 'level', 'building_name' : 'name'}
    lines = LayerMapping(FloorLine, inputshp, floor_mapper, transform=True)
    lines.save(strict=True, verbose=True)


def rename_building(old_name, new_name):
    building = FloorLine.objects.filter(building_name=old_name)
    for line in building:
        line.building_name = new_name
        line.save()


''' 
def build_floor(floorname, level):
    #builds floor of floorlines
    #flr = Floor()
    num = FloorLine.objects.all().count()
    linelist = []
    for i in range(num):
        line = FloorLine.objects.all()[i:i+1].get()
        linelist.append(line.linja)

    flr = Floor(level, linelist, floorname)
    flr.save()
'''
    
'''

from mapapp import load
load.read_lines('TIK_1.shp', 'EPSG_tik_1')


load.build_floor('TIK_1', 1)
'''