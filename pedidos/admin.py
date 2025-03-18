from .models import Pedidos, LineaPedido
from django.contrib import admin
# Register your models here.

'''class PedidosAdmin(admin.ModelAdmin):
    readonly_fields = ['user', 'created_at', 'total']
    
class LineaPedidosAdmin(admin.ModelAdmin):
    readonly_fields = ['user', 'producto_id', 'cantidad', 'created_at']'''
    
    
    
admin.site.register([Pedidos, LineaPedido])
'''admin.site.register(LineaPedido, LineaPedidosAdmin)'''