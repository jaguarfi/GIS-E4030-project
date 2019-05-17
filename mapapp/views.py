from django.shortcuts import render
from .models import FloorLine
from django.core.serializers import serialize

# Create your views here.

def ui(request):
    '''
    The python based backend logic of the mapservice.
    '''
    #Set showing 1st floors of the buildings as default option
    selectedfloor = '1st'
    #if request method is post, which in this app can only happen by the user changing the selected option of which floors are to be shown set selectedfloors accordingly
    if request.method == "POST":
        selectedfloor = request.POST['visibfloors']
    #filter data to be shown by the wanted floor level
    fpick = FloorLine.objects.filter(level=int(selectedfloor[0]))
    #transform the lines into geojson
    floor = serialize('geojson', fpick)
    #create context variable to send the data to the user as a http response
    context = {'floor' : floor, 'selectedfloor' : selectedfloor}
    return render(request, 'mapview.html', context)



