from django.conf.urls import url
from products.views import *

urlpatterns = [
    url(r'^product/(?P<pk>\d+)/$', Product.as_view(), name='product'),
    url(r'^products/', ProductsList.as_view(), name='products')
]
