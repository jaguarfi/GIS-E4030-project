from django.shortcuts import render
from .models import FloorLine
from django.core.serializers import serialize

# Create your views here.

def ui(request):
    floor = serialize('geojson', FloorLine.objects.all())
    context = {'floor' : floor, 'test' : 100}
    return render(request, 'mapview.html', context)



