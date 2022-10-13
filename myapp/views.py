from django.shortcuts import render
from .forms import studentform
def home(request):
    form=studentform
    return render(request,'home.html',{'form':form})
