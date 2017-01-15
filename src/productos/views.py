from django.shortcuts import get_object_or_404
from .serializers import ProductoSerializer
from .models import Producto
from rest_framework import generics

class ListaProductos(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_object(self):
         queryset = self.get_queryset()
         obj = get_object_or_404(
            qs,
            pk = self.kwargs['pk']
         )

# Create your views here.
