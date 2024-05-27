from django.shortcuts import render

def home(request):
    return render(request, "pages/home.html", {})

def contact(request):
    return render(request, "pages/contact.html", {})

def blog(request):
    return render(request, "pages/blog.html", {})

def about(request):
    return render(request, "pages/about.html", {})