from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Picture)
class PictureAdmin(admin.ModelAdmin):
        pass

