from django.conf.urls import url
from products.views import *

urlpatterns = [

    url(r'^$', ProductsList.as_view(), name='product'),
    url(r'^(?P<pk>\d+)/edit/$', ProductEdit.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/delete/$', ProductDelete.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/$', Product.as_view(), name='list')
]
