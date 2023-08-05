from django.contrib import admin
from .models import Advertisement
from django.db import models #For decimal.Decimal class

# Register your models here.
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'tradePossibility', 'createdDate', 'timeOfUpdate']
    list_filter = ['tradePossibility', 'timeOfCreate']
    list_editable = ['title', 'price', 'tradePossibility']
    actions = ['make_trade_False', 'make_trade_True', 'sale']
    fieldsets = (
        ('Общие', {
            'fields' : ('title', 'description')
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

    @admin.action(description='Скидка 17 процентов')
    def sale(self, request, queryset):
        for obj in queryset:
            #print(queryset[0].price-2, float(round(queryset[0].price*0.83, 2)), '---------------------------------------------------------')
            queryset.update(price = obj.price - 2)
            obj.save()

    sale.short_description = "Распродажа!"

admin.site.register(Advertisement, AdvertisementAdmin)