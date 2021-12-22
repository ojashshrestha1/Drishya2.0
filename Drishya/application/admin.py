from django.contrib import admin

from . import models
# Register your models here.

class ImageDetailsAdmin (admin.ModelAdmin):
    list_display= ['filename']

admin.site.register(models.ImageDetails, ImageDetailsAdmin)
