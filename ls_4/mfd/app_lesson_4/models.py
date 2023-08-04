from django.db import models

# Create your models here.
class Advertisement(models.Model): 
    title: str = models.CharField("Заголовок", max_length=128)
    description: str = models.TextField("Описание")
    price: float = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    tradePossibility: bool =  models.BooleanField("Торга", help_text="Отметьте, уместен ли торг")
    timeOfCreate = models.DateTimeField(auto_now_add = True)
    timeOfUpdate = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = "advertisements"

    def __str__(self):
        name = str(self.__class__)
        index = len(name) - name[::-1].find('.')
        return f"{name[index:-2]}(id={self.id}, title={self.title}, price={self.price})"