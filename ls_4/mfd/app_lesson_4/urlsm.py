from django.urls import path
from .views import indeh, top_sellers, advertisement_post#, post_detail

urlpatterns = [
    path('', indeh, name='main-page'),
    path('top-sellers', top_sellers, name='top-sellers'),
    path('advertisement-post/', advertisement_post, name="advertisement-post"),
    #path('post/<int:pk>/', post_detail, name='post_detail'),
]