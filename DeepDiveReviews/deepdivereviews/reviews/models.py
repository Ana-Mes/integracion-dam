from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from ckeditor.fields import RichTextField
from django.db.models.signals import m2m_changed

# Create your models here.

class DivingSpot(models.Model):
    # Modelo para el punto de inversión
    name = models.CharField(verbose_name="Nombre", max_length=200)
    description = RichTextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="divingspot")
    location = models.TextField(verbose_name="Localización", max_length=500)
    latitude = models.FloatField(verbose_name="Latitud")
    longitude = models.FloatField(verbose_name="Longitud")
    score = models.FloatField(verbose_name="Puntuación", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")

    class Meta:
        verbose_name = "punto de inmersión"
        verbose_name_plural = "puntos de inmersión"
        ordering = ['name']

    def __str__(self):
        return self.name

class Comment(models.Model):
    divingspot = models.ForeignKey('DivingSpot', on_delete=models.CASCADE, verbose_name="Punto de inmersión")
    content = models.TextField(verbose_name="Contenido", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor", related_name="user_comments")
    image = models.ImageField(verbose_name="Imagen", upload_to="comment", blank=True, null=True)
    score = models.IntegerField(verbose_name="Puntuación", default=0,
            validators=[
                MaxValueValidator(5),
                MinValueValidator(0)
            ]
        )

    class Meta:
        ordering = ['created']