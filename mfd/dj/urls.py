from django.urls import path 
from .views import index #импортируем функцию (собственную)

urlpatterns = [ #ключевое название
    path('', index)
]