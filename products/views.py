from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from django.http.request import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

from .models import Product
from .forms import ProductForm

# Create your views here.
class ProductListView(ListView):
    template_name = 'products/index.html'

    def get(self, request: HttpRequest):
        data = {
            "title": "Products",
            "products": Product.objects.all()
        }
        return render(request, self.template_name, data)
    
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
            form.save()
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