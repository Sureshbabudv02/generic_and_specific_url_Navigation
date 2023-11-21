from django.shortcuts import render

# Create your views here.

def mom(request):
    return render(request,'mom.html')

def master(request):
    return render(request,'master.html')