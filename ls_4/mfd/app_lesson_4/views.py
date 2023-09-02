from django.shortcuts import render, redirect #reverse -> from django.urls import reverse
from django.urls import reverse
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm
from django.db.models import Count

from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
# User = get_user_model()

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

import random

# Create your views here.

TEMPL_ROOT = "app_lesson_4/"


def index(request):
    advertisements = list(Advertisement.objects.all()) #Всё из таблицы Advertisement

    random.shuffle(advertisements)
    scrollAdvertisements = advertisements[:3]
    firstadver = scrollAdvertisements[0] #For aplications

    title = request.GET.get("search")
    print(request.GET.get("search"), "--------------")
    if title: #Если есть запрос
        advertisements = Advertisement.objects.filter(title__icontains = title)

    context = {"advertisements" : advertisements, 
               "scrollAdvertisements" : scrollAdvertisements, 
               "firstadver": firstadver,
               "title":title} 
    return render(request, TEMPL_ROOT+"index.html", context)

def advetrisements_detail(request, id):
    advertisement = Advertisement.objects.get(id=id)
    context = {
        "adv" : advertisement
    }
    return render(request, TEMPL_ROOT+"advertisement.html", context)

def top_sellers(request):
    users = User.objects.annotate(
        adv_count = Count("advertisement")
    ).order_by("-adv_count")
    context = {
        "best_authors": users if len(users) < 10 else list(users)[:10]
    }
    return render(request, TEMPL_ROOT+"top-sellers.html", context)

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