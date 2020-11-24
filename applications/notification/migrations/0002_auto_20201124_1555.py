# Generated by Django 3.0.7 on 2020-11-24 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201124_1555'),
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='user',
        ),
        migrations.AddField(
            model_name='notification',
            name='schools',
            field=models.ManyToManyField(to='user.School', verbose_name='Facultades'),
        ),
    ]