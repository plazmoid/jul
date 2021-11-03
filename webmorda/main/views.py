from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')


def about_project(request):
    return render(request, 'main/about_project.html')


def test(request):
    return render(request, 'main/test.html')