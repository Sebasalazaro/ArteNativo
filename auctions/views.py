from django.http import HttpRequest
from django.views import View
from django.views.generic import TemplateView
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404

from .models import Auction
from .forms import AuctionForm
from products.models import Product

# Create your views here.
class AuctionListView(TemplateView):
    template_name = 'auctions/view.html'

    def get(self, request: HttpRequest):
        auctions = Auction.objects.filter(bid_end_time__gt=timezone.now())
        data = {
            'title': 'Auctions',
            'auctions': auctions
        }
        return render(request, self.template_name, data)

class AuctionCreateView(View):
    template_name = 'auctions/form_.html'

    def get(self, request: HttpRequest, pk):
        product = get_object_or_404(Product, id=pk)
        form = AuctionForm()
        data = {
            'title': f'{product.name} Auction',
            'product': product,
            'form': form
        }
        return render(request, self.template_name, data)
    
    def post(self, request: HttpRequest, pk):
        product = get_object_or_404(Product, id=pk)
        form = AuctionForm(request.POST)
        if form.is_valid():
            auction = form.save(commit=False)
            auction.product = product
            auction.current_price = auction.starting_price
            auction.save()
            return redirect('auction_list')
        data = {
            'title': f'{product.name} Auction',
            'product': product,
            'form': form
        }
        return render(request, self.template_name, data)