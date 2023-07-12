from django.contrib import admin
from . import models



@admin.register(models.Mind, models.Color, models.Shape, models.Other)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", )

    def used_by(self, obj):
        return obj.rooms.count()

    pass



# Register your models here.
@admin.register(models.SearchHistory)
class ItemAdmin(admin.ModelAdmin):
        pass



# Register your models here.
@admin.register(models.Picture)
class PictureAdmin(admin.ModelAdmin):
        pass


