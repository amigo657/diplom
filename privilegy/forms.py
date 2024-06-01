from django import forms
from .models import Privilege

class PrivilegePurchaseForm(forms.Form):
    privilege = forms.ModelChoiceField(queryset=Privilege.objects.all(), empty_label="Выберите привилегию")


class PaymentForm(forms.Form):
    card_number = forms.CharField(max_length=16, required=True)
    card_name = forms.CharField(max_length=100, required=True)
    expiry_date = forms.CharField(max_length=5, required=True)
    cvv = forms.CharField(max_length=3, required=True)
