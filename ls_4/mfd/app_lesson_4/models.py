from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

# Create your models here.
class Advertisement(models.Model): 
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    tradePossibility =  models.BooleanField("Торга", help_text="Отметьте, уместен ли торг")
    timeOfCreate = models.DateTimeField(verbose_name='Время создания',auto_now_add = True)
    timeOfUpdate = models.DateTimeField(verbose_name='Время обновления', auto_now = True)
    author = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)#, default=models.ForeignKey(AdvertisementAdmin, verbose_name="Пользователь", on_delete=models.CASCADE))
    image = models.ImageField("Изображение", upload_to="advertisements/")
    
    @admin.display(description="Дата создания")
    def createdDate(self):
        created_time = self.timeOfCreate.strftime('%H:%M:%S')
        if self.timeOfCreate.date() == timezone.now().date():
            return format_html(
                "<span style='color: #2E8B57; font-weight: bold;'>Сегодня в {}</span>", created_time
            )
        return self.timeOfCreate.strftime('%d.%m.%Y')# в %H:%M:%S')
    
    @admin.display(description="Дата обновления")
    def updatedDate(self):
        created_time = self.timeOfUpdate.strftime('%H:%M:%S')
        if self.timeOfUpdate.date() == timezone.now().date():
            return format_html(
                f"<span style='color: #4682B4; font-weight: bold;'>Сегодня в {created_time}</span>"
            )
        return self.timeOfUpdate.strftime('%d.%m.%Y')
    
    @admin.display(description="Изображение")
    def miniImage(self):
        if self.image:
            return format_html(
                f"<img src='{settings.MEDIA_URL}{self.image}' style='width: 70px; height = 45px;' />"
            )
        else:
            return format_html(
                "<span style='opacity: 0.5;'>NO IMAGE</span>"
            )

    class Meta:
        db_table = "advertisements"

    def __str__(self):
        name = str(self.__class__)
        index = len(name) - name[::-1].find('.')
        return f"{name[index:-2]}(id={self.id}, title={self.title}, price={self.price})"