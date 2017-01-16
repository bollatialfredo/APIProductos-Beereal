from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView
    )

from django.shortcuts import get_object_or_404
from .serializers import ProductSerializer
from .models import Product


class ProductsList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_object(self):
         queryset = self.get_queryset()
         obj = get_object_or_404(
            qs,
            pk = self.kwargs['pk']
         )




class ProductEdit(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDelete(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class Product(RetrieveAPIView): #si esto no esta al final no anda ?????
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
