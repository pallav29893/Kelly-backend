from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request,'about us.html')

def contact(request):
    return render(request, 'contact us.html')