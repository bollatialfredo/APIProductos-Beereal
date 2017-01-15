from django.conf.urls import url
from productos.views import *

urlpatterns = [
    url(r'^productos/', ListaProductos.as_view(), name='productos')
]
