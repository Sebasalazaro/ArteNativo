# maps/views.py
from django.shortcuts import render
from products.models import Product
from django.views import View
from django.http import JsonResponse


class MapView(View):
    template_name = 'map_view.html'

    def get(self, request):
        # Obtenemos todos los productos y sus direcciones
        products = Product.objects.all()
        context = {
            'products': products,
        }
        return render(request, self.template_name, context)

class ProductJsonView(View):
    def get(self, request):
        # Obtenemos todos los productos con sus direcciones y demás datos necesarios
        products = Product.objects.all()

        product_list = [
            {
                'name': product.name,
                'address': product.address,
                'description': product.description,
                'price': product.price,
                # Incluye cualquier otra información relevante aquí
            }
            for product in products
        ]
        
        return JsonResponse({'products': product_list})