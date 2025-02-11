# Generated by Django 4.2 on 2023-05-03 08:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='Puntuación'),
        ),
        migrations.AlterField(
            model_name='divingspot',
            name='score',
            field=models.IntegerField(default=0, verbose_name='Puntuación'),
        ),
    ]
