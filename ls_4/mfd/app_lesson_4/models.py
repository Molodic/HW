from django.db import models

# Create your models here.
class Advertisement(models.Model): 
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    tradePossibility =  models.BooleanField("Торга", help_text="Отметьте, уместен ли торг")
    timeOfCreate = models.DateTimeField(auto_now_add = True)
    timeOfUpdate = models.DateTimeField(auto_now = True)
