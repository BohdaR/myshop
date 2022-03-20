from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'phone_number', 'city', 'delivery_method', 'pay_method']
        widgets = {
            'delivery_method': forms.RadioSelect(attrs={'class': 'order-chekbox'}),
            'pay_method': forms.RadioSelect(attrs={'class': 'order-chekbox'}),
        }