from django import forms

from .models import Product, Comment

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'rating']
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, f'{i} estrella{"s" if i > 1 else ""}') for i in range(1, 6)]),
        }
