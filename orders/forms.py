from django import forms
from django.utils.safestring import mark_safe


class CartAddForm(forms.Form):
    quantity = forms.IntegerField(label=mark_safe('Quantity'), min_value=1, max_value=9, initial=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))


class CouponApplyForm(forms.Form):
	code = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control'}))