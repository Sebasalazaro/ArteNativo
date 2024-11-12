from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from django.http import JsonResponse
from django.http.request import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
import requests

from .serializer import ProductSerializer
from .models import Product
from .forms import ProductForm

GOOGLE_MAPS_API_KEY = 'AIzaSyC7V_wGnvGMb8DYN-xTjmSgGCAxM5DwDGU'  # Sustituye con tu clave de API

# Create your views here.
class ProductListView(ListView):
    template_name = 'products/index.html'

    def get(self, request: HttpRequest):
        products = Product.objects.all()

        data = {
            "title": "Products",
            "products": products
        }
        return render(request, self.template_name, data)
    
class ProductJsonView(View):
    def get(self, request: HttpRequest):
        products = Product.objects.all()

        product_list = [
            {
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': product.price,
                'image_url': product.image.url if product.image else None,
                'address': product.address if product.address else None,
            }
            for product in products
        ]
        data = { 'products': product_list }
        return JsonResponse(data)

class ProductCreateView(View):
    template_name = 'products/form_.html'
    
    def get(self, request: HttpRequest):
        form = ProductForm()
        data = { 
            'title': 'New Product', 
            'form': form,
        }
        return render(request, self.template_name, data)
    
    def post(self, request: HttpRequest):
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('product_list')
        data = { 
            'title': 'New Product', 
            'form': form, 
        }
        return render(request, self.template_name, data)
     
class ProductReadView(View):
    template_name = 'products/view.html'

    def get(self, request: HttpRequest, pk):
        product = get_object_or_404(Product, pk=pk)
        data = {
            "title": self.template_title,
            "product": product
        }
        return render(request, self.template_name, data)

class ProductUpdateView(View):
    template_name = 'products/form_.html'

    def get(self, request: HttpRequest, pk=None):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(instance=product)
        data = { 
            'title': 'Edit Product', 
            'form': form,
        }
        return render(request, self.template_name, data)
        
    def post(self, request: HttpRequest, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        data = {
            "title": 'Edit Product',
            "form": form
        }
        return render(request, self.template_name, data)

class ProductDeleteView(View):
    template_name = 'products/confirm.html'

    def get(self, request: HttpRequest, pk):
        product = get_object_or_404(Product, pk=pk)
        data = {
            'title': 'Delete Product',
            'product': product
        }
        return render(request, self.template_name, data)

    def post(self, request: HttpRequest, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()    
        return redirect('product_list')
    
class ProductSearchView(View):
    template_name = 'products/results.html'

    def get(self, request: HttpRequest):
        query = request.GET.get('q')
        if query:
            products = Product.objects.filter(name__icontains=query)
        else:
            products = []
        data = {
            'products': products,
            'query': query
        }
        return render(request, self.template_name, data)
    


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer