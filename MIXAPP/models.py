from django.db import models
from django.utils import timezone

class Musica(models.Model):
        author = models.ForeignKey('auth.User')
        title = models.CharField(max_length=200)
        text = models.TextField()
        created_date = models.DateTimeField(
                default=timezone.now)
        published_date = models.DateTimeField(
                blank=True, null=True)

        def agregar(self):#funcion agregar disco
            self.published_date = timezone.now()
            self.save()

        def __str__(self):#retornamos texto con __str__ y lo que se retorna es el titulo
            return self.title
