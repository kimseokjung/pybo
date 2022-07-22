from django import forms
from .models import Products


class ProductPostForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product_board']
        labels = {
            'product_board': '상세 설명',
        }
