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
    score = models.IntegerField(verbose_name="Puntuación", default=0,
            validators=[
                MaxValueValidator(5),
                MinValueValidator(0)
            ]
        )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")

    class Meta:
        verbose_name = "reseña"
        verbose_name_plural = "reseñas"
        ordering = ['name']

    def __str__(self):
        return self.name

class Comment(models.Model):
    divingspot = models.ForeignKey('DivingSpot', on_delete=models.CASCADE, verbose_name="Localización")
    title = models.CharField(verbose_name="Título", max_length=200)
    content = models.TextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")

    class Meta:
        ordering = ['created']

class Thread(models.Model):
    users = models.ManyToManyField(User, related_name='threads')
    comments = models.ManyToManyField(Comment)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']


def comments_changed(sender, **kwargs):
    instance = kwargs.pop("instance", None)
    action = kwargs.pop("action", None)
    pk_set = kwargs.pop("pk_set", None)
    print(instance, action, pk_set)

    false_pk_set = set()
    if action is "pre_add":
        for comment_pk in pk_set:
            comment = Comment.objects.get(pk=comment_pk)
            if comment.user not in instance.users.all():
                print("Ups, ({}) no forma parte del hilo".format(comment.user))
                false_pk_set.add(comment_pk)
    
    # Buscar los mensajes de false_pk:set que no están en pk_set y los borramos de pk_set
    pk_set.difference_update(false_pk_set)

    # Forzar la actualización haciendo save
    instance.save()

m2m_changed.connect(comments_changed, sender=Thread.comments.through)