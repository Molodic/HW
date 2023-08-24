from django.contrib import admin
from .models import Advertisement
from django.db import models 
from decimal import Decimal #For decimal.Decimal class

# Register your models here.
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'tradePossibility', 'createdDate', 'updatedDate', "miniImage"]
    list_filter = ['tradePossibility', 'timeOfCreate']
    list_editable = ['title', 'price', 'tradePossibility']
    actions = ['make_trade_False', 'make_trade_True', 'sale']
    fieldsets = (
        ('Общие', {
            'fields' : ("author", 'title', 'description')
        }), 
        ('Финансы', {
            'fields' : ('price', 'tradePossibility'),
            'classes' : ['collapse']
        }), 
        )
    
    @admin.action(description='Добавить возможность торга')
    def make_trade_True(self, request, queryset):
        queryset.update(tradePossibility = True)
        for obj in queryset:
            obj.save()

    @admin.action(description='Убрать возможность торга')
    def make_trade_False(self, request, queryset):
        queryset.update(tradePossibility = False)
        for obj in queryset:
            obj.save()

    @admin.action(description='Скидка 17 процентов (-2 рубля)')
    def sale(self, request, queryset):
        for obj in queryset:
            print(obj)
            obj.price = Decimal(round(float(obj.price) * 0.83, 1)-0.01)
            obj.save()

    sale.short_description = f"Распродажа!" 

admin.site.register(Advertisement, AdvertisementAdmin)