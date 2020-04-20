from django import forms
from django.forms import ModelForm
from .models import Pembayaranform

class Pembayaran(ModelForm):
    class Meta:
        model = Pembayaranform
        fields='__all__'