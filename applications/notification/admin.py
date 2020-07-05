from django.contrib import admin

# Register your models here.

from  .models import Notification,Notice

admin.site.register(Notification)
admin.site.register(Notice)