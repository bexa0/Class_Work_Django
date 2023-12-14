from django import forms
from app.models import Product


class ProductCreateModelForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('slug',)
        widgets = {
            'description': forms.Textarea()
        }


class ProductUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('slug',)
        widgets = {
            'description': forms.Textarea()
        }