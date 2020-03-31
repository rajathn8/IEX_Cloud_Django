from django import forms
from .models import Stock
from django.forms import ModelForm

class StockForm(forms.ModelForm):

	class Meta:

		model = Stock
		fields = ['ticker']