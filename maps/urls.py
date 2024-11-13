# maps/urls.py
from django.urls import path
from .views import MapView, ProductJsonView

urlpatterns = [
    path('', MapView.as_view(), name='map_view'),
    path('products-json/', ProductJsonView.as_view(), name='products_json'),
]
