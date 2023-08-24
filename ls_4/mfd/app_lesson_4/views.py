from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm

# Create your views here.

def index(request):
    advertisements = Advertisement.objects.all() #Всё из таблицы Advertisement
    context = {"advertisements" : advertisements} 
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            new_advertisement = form.save(commit=False)
            new_advertisement.author = request.user
            new_advertisement.save()
                # No need, cuz now we have "modelForm" - no simple "Form" any more :)
                # advertisement = Advertisement(**form.cleaned_data) 
                # advertisement.author = request.user
                # advertisement.save()
            url = reverse("main-page")
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {"form" : form}
    return render(request, "advertisement-post.html", context)