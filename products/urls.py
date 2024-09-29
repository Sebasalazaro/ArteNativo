from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('new/', ProductCreateView.as_view(), name='product_create'),
    path('view/<int:pk>/', ProductReadView.as_view(), name='product_read'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
]