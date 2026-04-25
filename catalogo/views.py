from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Productos, Categoria
from .serializers import ProductosSerializers, CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializers

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# Con esto permito que cualqiera vea, pero solo yo puedo editar
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]