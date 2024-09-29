from django.views import View
from django.views.generic import TemplateView
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

from products.models import Item, Product

# Create your views here.
class CartListView(TemplateView):
    template_name = 'cart/view.html'

    def get(self, request: HttpRequest):
        if not request.user.is_authenticated:
            return redirect('login')
        
        items = Item.objects.filter(user=request.user.id)
        data = {
            'title': 'Shopping Cart',
            'items': items
        }
        return render(request, self.template_name, data)

class CartCreateView(View):
    def get(self, request: HttpRequest, pk):
        if not request.user.is_authenticated:
            return redirect('login')
        product = Product.objects.get(id=pk)
        item, created = Item.objects.get_or_create(
            user=request.user,
            product=product,
            defaults={'price_at_purchase': product.price, 'quantity': 1}
        )
        if not created:
            item.quantity += 1
            item.save()
        return redirect('product_list')
    
class CartUpdateView(View):
    def post(self, request: HttpRequest, pk):
        item = get_object_or_404(Item, id=pk, user=request.user)
        new_quantity = request.POST.get('quantity')
        if new_quantity and new_quantity.isdigit() and int(new_quantity) > 0:
            item.quantity = int(new_quantity)
            item.save()
        return redirect('view_cart')
    
class CartDeleteView(View):
    def post(self, request: HttpRequest, pk):
        item = get_object_or_404(Item, id=pk, user=request.user)
        item.delete()
        return redirect('view_cart')