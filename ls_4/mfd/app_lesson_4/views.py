from django.shortcuts import render, reverse, redirect #reverse -> from django.urls import reverse
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.

TEMPL_ROOT = "app_lesson_4/"

def index(request):
    advertisements = Advertisement.objects.all() #Всё из таблицы Advertisement
    context = {"advertisements" : advertisements} 
    return render(request, TEMPL_ROOT+"index.html", context)

def top_sellers(request):
    return render(request, TEMPL_ROOT+"top-sellers.html")

@login_required(login_url=reverse_lazy("login"))
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
    return render(request, TEMPL_ROOT+"advertisement-post.html", context)