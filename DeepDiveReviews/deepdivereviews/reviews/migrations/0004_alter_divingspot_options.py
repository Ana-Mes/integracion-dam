# Generated by Django 4.1.7 on 2023-05-13 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_comment_divingspot_delete_thread'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='divingspot',
            options={'ordering': ['name'], 'verbose_name': 'punto de inmersión', 'verbose_name_plural': 'puntos de inmersión'},
        ),
    ]
