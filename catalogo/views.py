from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Productos, Categoria
from .serializers import ProductosSerializers, CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    # OPTIMIZADO: select_related une productos y categorías en una sola consulta rápida
    queryset = Productos.objects.select_related('categoria').all()
    serializer_class = ProductosSerializers
    # Con esto permito que cualquiera vea, pero solo yo puedo editar (Movido al lugar correcto)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]