from django.urls import path
from .views import index, top_sellers, advertisement_post, advetrisements_detail#, post_detail

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers', top_sellers, name='top-sellers'),
    path('advertisement-post/', advertisement_post, name="advertisement-post"),
    path("advertisement/<int:id>", advetrisements_detail, name="advertisement")
    #path('post/<int:pk>/', post_detail, name='post_detail'),
]