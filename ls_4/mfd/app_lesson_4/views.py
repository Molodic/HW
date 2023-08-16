from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement

# Create your views here.

def indeh(request):
    advertisements = Advertisement.objects.all() #Всё из таблицы Advertisement
    context = {"advertisements" : advertisements} 
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')
