from django.db import models
from django.contrib import admin
from django.utils.html import format_html

# Create your models here.
class Advertisement(models.Model): 
    title: str = models.CharField("Заголовок", max_length=128)
    description: str = models.TextField("Описание")
    price: float = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    tradePossibility: bool =  models.BooleanField("Торга", help_text="Отметьте, уместен ли торг")
    timeOfCreate = models.DateTimeField(verbose_name='Время создания',auto_now_add = True)
    timeOfUpdate = models.DateTimeField(verbose_name='Время обновления', auto_now = True)
    
    @admin.display(description="Дата создания")
    def createdDate(self):
        from django.utils import timezone
        created_time = self.timeOfCreate.strftime('%H:%M:%S')
        if self.timeOfCreate.date() == timezone.now().date():
            return format_html(
                "<span style='color: green; font-weight: bold;'>Сегодня в {}</span>", created_time
            )
        return self.timeOfCreate.strftime('%d.%m.%Y')# в %H:%M:%S')

    class Meta:
        db_table = "advertisements"

    def __str__(self):
        name = str(self.__class__)
        index = len(name) - name[::-1].find('.')
        return f"{name[index:-2]}(id={self.id}, title={self.title}, price={self.price})"