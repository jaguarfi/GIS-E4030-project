from django.contrib.gis.db import models


    
class FloorLine(models.Model):
    '''
    The basic class used to store data in the current data model - each entry is a linestring object, that also belongs to a building with a defined name,
    belonds to some floor (1+). The attribute layer is used while moving the data to the database and is currently somewhat superfluous (delete later?).
    '''
    layer = models.IntegerField()
    level = models.IntegerField()
    linja = models.LineStringField()
    building_name = models.CharField(max_length=30)





