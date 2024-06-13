from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def mma_view(request):
    return render(request, 'mma.html')