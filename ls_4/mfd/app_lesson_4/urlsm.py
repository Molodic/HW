from django.urls import path
from .views import indeh, top_sellers#, post_detail

urlpatterns = [
    path('', indeh, name='main-page'),
    path('top-sellers', top_sellers, name='top-sellers')
    #path('post/<int:pk>/', post_detail, name='post_detail'),
]