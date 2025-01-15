from django.contrib import admin
from .models import Belt, Technique

@admin.register(Belt)
class BeltAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Technique)
class TechniqueAdmin(admin.ModelAdmin):
    list_display = ('name', 'belt')
    list_filter = ('belt',)
    search_fields = ('name',)
