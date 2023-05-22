from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "page/index.html")


def about(request):
    return render(request, "page/about.html")


def post(request):
    return render(request, "page/post.html")


def contact(request):
    return render(request, "page/contact.html")


def contact_submit(request):
    return render(request, "page/contact.html")

def login(request):
    return render(request, "page/auth/login.html")

def register(request):
    return render(request, "page/auth/register.html")
