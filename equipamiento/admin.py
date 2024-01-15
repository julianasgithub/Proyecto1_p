from django.contrib import admin
from .models import  Equipamiento
# Register your models here.



class EquipamientoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')


admin.site.register(Equipamiento, EquipamientoAdmin)