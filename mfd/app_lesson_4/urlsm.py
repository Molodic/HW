from django.urls import path
from .views import indeh#, post_detail

urlpatterns = [
    path('lesson_4/', indeh, name='indeh'),
    #path('post/<int:pk>/', post_detail, name='post_detail'),
]