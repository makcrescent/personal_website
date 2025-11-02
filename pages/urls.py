from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page_view),
    path('aboutus/', views.about_page_view),
]
