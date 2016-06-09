from django.contrib import admin
from .models import Proveedor, Startup, Categoria

# Register your models here.

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'pagina_web', 'logo')

admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Startup)
admin.site.register(Categoria)