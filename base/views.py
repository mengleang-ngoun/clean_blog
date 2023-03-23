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
    print(form)
    return render(request, "page/contact.html")
