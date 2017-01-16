from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

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

class Product(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
# Create your views here.
