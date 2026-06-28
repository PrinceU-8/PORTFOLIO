from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def works(request):
    return render(request, 'works.html')

def mworks(request):
    return render(request, 'mworks.html')

def contact(request):
    return render(request, 'contact.html')