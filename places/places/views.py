import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Place

# Create your views here.


def PlaceList(request):
    queryset = Place.objects.all()
    context = list(queryset.values('id', 'name'))
    return JsonResponse(context, safe=False)

def PlaceCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        place = Place()
        place.name = data_json['name']
        place.save()
        return HttpResponse("successfully created place")
    else: 
        return HttpResponse("request is not post")
