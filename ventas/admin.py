from django.contrib import admin
from .models import productos,categoria, ventas
# Register your models here.

admin.site.register(productos)
admin.site.register(categoria)
admin.site.register(ventas)
