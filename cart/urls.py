from django.urls import path
from .views import *

urlpatterns = [
    path('', CartListView.as_view(), name='view_cart'),
    path('new/<int:pk>/', CartCreateView.as_view(), name='new_cart_item'),
    path('update/<int:pk>/', CartUpdateView.as_view(), name='update_cart_item'),
    path('delete/<int:pk>/', CartDeleteView.as_view(), name='remove_cart_item'),
]