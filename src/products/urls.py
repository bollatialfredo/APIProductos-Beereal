from django.conf.urls import url
from products.views import *

urlpatterns = [
    url(r'^edit/(?P<pk>\d+)/$', ProductEdit.as_view(), name='product'),
    url(r'^delete/(?P<pk>\d+)/$', ProductDelete.as_view(), name='product'),
    url(r'^product/(?P<pk>\d+)/$', Product.as_view(), name='product'),
    url(r'^products/', ProductsList.as_view(), name='products')
]
