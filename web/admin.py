from django.contrib import admin
from .models import Producto, Categoria

# Register your models here.

#admin.site.register(Producto)
admin.site.register(Categoria)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio','categoria', 'fecha_registro')
    list_editable = ('precio',)
    
    
