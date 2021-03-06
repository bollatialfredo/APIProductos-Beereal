from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^api/products/', include('products.urls', namespace='products')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += [
    url(r'^api/auth', include('rest_framework.urls', namespace='rest_framework')),
]
