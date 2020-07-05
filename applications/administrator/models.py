from django.db import models

# Create your models here.

class Admin(models.Model):
    """Model definition for Admin."""

    name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellido', max_length=50)
    email = models.EmailField('Email', max_length=254)
    password = models.CharField('Contraseña', max_length=50)

    class Meta:
        """Meta definition for Admin."""
        db_table = 'Admin'
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'

    def __str__(self):
        """Unicode representation of Admin."""
        return self.name


