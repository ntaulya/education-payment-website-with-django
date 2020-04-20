from . import forms
from django.shortcuts import render
from .forms import Pembayaranform

#Create your views here.
def index(request):
    return render(request, 'index.html')

def pembayaran_function(request):
    form=Pembayaranform()
    if request.method=='POST':
        form=Pembayaranform(request.POST)
        # if forms.is_valid():
        # form.save()
    context={'form':form}
    return render(request, 'pembayaran.html', context)
