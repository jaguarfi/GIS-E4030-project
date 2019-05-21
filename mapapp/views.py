from django.shortcuts import render
from .models import FloorLine
from django.core.serializers import serialize
from django.http  import HttpResponse

# Create your views here.

def ui(request):
    return render(request, 'mapview.html')

def TIK(request, floor):
    selectedfloor = floor
    if request.method == "POST":
        selectedfloor = request.POST['visibfloors']
    fpick = FloorLine.objects.filter(level=int(selectedfloor),building_name='TIK_TALO')
    TIK_floor = serialize('geojson', fpick)
    context = {'floor' : TIK_floor, 'selectedfloor' : selectedfloor}
    return HttpResponse(TIK_floor,content_type='json')

def TUAS(request, floor):
    selectedfloor = floor
    if request.method == "POST":
        selectedfloor = request.POST['visibfloors']
    fpick = FloorLine.objects.filter(level=int(selectedfloor),building_name='TUAS_TALO')
    TUAS_floor = serialize('geojson', fpick)
    context = {'floor' : TUAS_floor, 'selectedfloor' : selectedfloor}
    return HttpResponse(TUAS_floor,content_type='json')
   


