from django.db import models

# Create your models here.

class School(models.Model):
    """Model definition for School."""

    name = models.CharField('Nombre', max_length=50)


    class Meta:
        """Meta definition for School."""

        db_table = 'School'
        verbose_name = 'Facultad'
        verbose_name_plural = 'Facultades'

    def __str__(self):
        """Unicode representation of School."""
        return self.name


class User(models.Model):
    """Model definition for User."""

    name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellido', max_length=50)
    dni = models.CharField('DNI', max_length=50, null=True)
    email = models.EmailField('Email', max_length=254)
    password = models.CharField('Contraseña', max_length=50)
    token = models.CharField('Token', max_length=50)
    school = models.ManyToManyField(School, verbose_name = 'Facultad/es')

    class Meta:
        """Meta definition for User."""

        db_table = 'User'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        """Unicode representation of User."""
        return self.name

