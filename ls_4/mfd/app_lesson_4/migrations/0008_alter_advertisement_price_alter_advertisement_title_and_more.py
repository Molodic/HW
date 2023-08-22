# Generated by Django 4.2.3 on 2023-08-22 23:40

import app_lesson_4.models
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_lesson_4', '0007_alter_advertisement_tradepossibility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[app_lesson_4.models.MinValueValidatorFix(Decimal('0.01000000000000000020816681711721685132943093776702880859375'))], verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.CharField(max_length=64, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='tradePossibility',
            field=models.BooleanField(help_text='Отметьте, уместен ли торг', verbose_name='Торг'),
        ),
    ]