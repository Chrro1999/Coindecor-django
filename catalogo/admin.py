from django.contrib import admin
from .models import Categoria, Productos, ImagenProducto, Pedido, ItemPedido

# --- INLINES ---

# Permite subir múltiples imágenes desde la ficha del producto
class ImagenProductoInline(admin.TabularInline):
    model = ImagenProducto
    extra = 3 # Muestra 3 espacios para subir fotos de inicio

# Permite ver los productos comprados dentro de la ficha del pedido
class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 0 
    readonly_fields = ('producto', 'cantidad', 'precio_unitario')

# --- CONFIGURACIONES DE ADMIN ---

@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria', 'stock')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'descripcion')
    inlines = [ImagenProductoInline] # Aquí activamos la galería de fotos

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_completo', 'total_pagado', 'estado', 'fecha_creacion')
    list_filter = ('estado', 'fecha_creacion')
    search_fields = ('nombre_completo', 'email', 'transaction_id')
    inlines = [ItemPedidoInline]

# Registros simples
admin.site.register(Categoria)