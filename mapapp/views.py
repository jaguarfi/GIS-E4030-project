from django.shortcuts import render
from .models import FloorLine
from django.core.serializers import serialize

# Create your views here.

def ui(request):
    selectedfloor = '1st'
    if request.method == "POST":
        selectedfloor = request.POST['visibfloors']
    fpick = FloorLine.objects.filter(level=int(selectedfloor[0]))
    floor = serialize('geojson', fpick)
    context = {'floor' : floor, 'selectedfloor' : selectedfloor}
    return render(request, 'mapview.html', context)



