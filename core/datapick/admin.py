from django.contrib import admin

from . import models

@admin.register(models.Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'price',
        'location',
        'date'
    ]

