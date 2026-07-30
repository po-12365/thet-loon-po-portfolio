from django.shortcuts import render


def home(request):
    return render(request, "portfolio/home.html")


def food(request):
    return render(request, "portfolio/food.html")


def australia(request):
    return render(request, "portfolio/australia.html")


def timeline(request):
    return render(request, "portfolio/timeline.html")


def journey(request):
    return render(request, "portfolio/journey.html")