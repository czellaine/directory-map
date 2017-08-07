from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.db.models import Q
from django.forms.models import model_to_dict
from django.core import serializers

from app.models import Item, Location

def index(request):
    return render(request, 'app/index.html')

def search(request):
    query = request.GET['q']
    field = request.GET['filter']
    if field == 'author':
        results = Item.objects.filter(book__author__name__icontains=query)
    elif field == 'title':
        results = Item.objects.filter(book__title__title__icontains=query)
    elif field == 'call_number':
        results = Item.objects.filter(book__call_number__call_number__icontains=query)
    else:
        results = Item.objects.filter(
            Q(book__author__name__icontains=query) |
            Q(book__title__title__icontains=query) |
            Q(book__call_number__call_number__icontains=query)
        )
    return render(request, 'app/index.html',
        {'results': results})

def getLocation(request):
    acc_no = request.GET.get('acc_no')
    item = Item.objects.get(accession_number__exact=acc_no)
    location = Location.objects.get(id__exact=item.location_id)
    data = {
        'location': location.location,
        'file': location.filename.url
    }
    return JsonResponse(data)
