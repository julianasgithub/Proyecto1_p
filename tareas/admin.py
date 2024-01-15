from django.contrib import admin
from .models import Tarea

# Register your models here.
class TareaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
admin.site.register(Tarea, TareaAdmin)