from rest_framework import serializers
from .models import Productos, Categoria, ImagenProducto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

#serializer para las imagenes adicionales del producto
class ImagenProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenProducto
        fields = ['id', 'imagen', 'descripcion']


class ProductosSerializers(serializers.ModelSerializer):
    categoria_nombre = serializers.ReadOnlyField(source='categoria.nombre')#Se visualiza el nombre de la categoria y no el ID
    
    imagenes = ImagenProductoSerializer(many=True, read_only=True) # Agrego las imágenes adicionales al serializer del producto
    
    class Meta:
        model = Productos
        fields = [
            'id', 
            'nombre', 
            'descripcion', 
            'precio',
            'imagen', 
            'stock', 
            'categoria', 
            'categoria_nombre', 
            'imagenes'
        ]