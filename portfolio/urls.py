from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('food/', views.food, name='food'),
    path("australia/", views.australia, name="australia"),
    path("timeline/", views.timeline, name="timeline"),
    path("journey/", views.journey, name="journey"),
]