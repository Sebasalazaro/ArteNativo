from django.urls import path
from .views import *

urlpatterns = [
    path('', AuctionListView.as_view(), name='auction_list'),
    path('new/<int:pk>/', AuctionCreateView.as_view(), name='auction_create'),
]