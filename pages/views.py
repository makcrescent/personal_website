# pages/views.py
from django.shortcuts import render


def home_page_view(request):
    return render(request, "pages/home.html")


def about_page_view(request):
    context = {"name": "Aslam Khan"}
    return render(request, "pages/about.html", context)
