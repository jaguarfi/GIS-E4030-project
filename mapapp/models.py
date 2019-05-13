from django.contrib.gis.db import models



class WorldBorder(models.Model):
    #The geodjango tutorial model for world borders, not actually needed for the project
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name


#borked
#class Floor(models.Model):
    #level: 1+ and needed for vertical topology. We'll define background map/outside as level zero and the converted CAD floors are 1+
    #accept nulls and blank, as they are loaded by a script that creates the objects first with geometry and sequentially adds the others
    #level = models.IntegerField()
    #floorgeom = models.MultiLineStringField()
    #name = models.CharField(max_length=30)
    
class FloorLine(models.Model):
    '''
    temporary class to help create floors
    '''
    layer = models.IntegerField()
    level = models.IntegerField()
    linja = models.LineStringField()
    building_name = models.CharField(max_length=30)





