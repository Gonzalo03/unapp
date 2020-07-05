from django.db import models

from model_utils.models import TimeStampedModel

from applications.administrator.models import Admin
from applications.user.models import User

# Create your models here.

class Notification(TimeStampedModel):
    """Model definition for Notification."""

    tittle = models.CharField('Titulo', max_length=50)
    body = models.CharField('Cuerpo', max_length=50)
    icon = models.ImageField('Icono', upload_to='iconos', height_field=None, width_field=None, max_length=None)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE, verbose_name = 'Administrador')
    user = models.ManyToManyField(User, verbose_name = 'Usuario')
    

    class Meta:
        """Meta definition for Notification."""

        db_table = 'Notification'
        verbose_name = 'Notificación'
        verbose_name_plural = 'Notificaciones'

    def __str__(self):
        """Unicode representation of Notification."""
        return self.tittle

class Notice(TimeStampedModel):

    tittle = models.CharField('Titulo', max_length=50)
    cover = models.ImageField('Portada', upload_to='portada', height_field=None, width_field=None, max_length=None)
    description = models.CharField('Descripcion', max_length=50)
    body = models.CharField('Cuepo', max_length=200)
    footer = models.CharField('Footer', max_length=50)

    class Meta:
        """Meta definition for Notice."""

        db_table = 'Noticia'
        verbose_name = 'Noticias'
        verbose_name_plural = 'Noticias'

    
        def __str__(self):
            return self.tittle
        