from django.db.models import Q

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView
    )

from .serializers import ProductSerializer
from .models import Product as ProductModel


class ProductsList(ListCreateAPIView):
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'condition']

    def get_queryset(self, *args, **kwargs):
        queryset_list = ProductModel.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
            Q(name__icontains = query)
            ).distinct()
        return queryset_list



class ProductEdit(UpdateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer


class ProductDelete(DestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer


class Product(RetrieveAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
