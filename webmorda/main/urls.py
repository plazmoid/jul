from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about-us', views.about),
    path('contact', views.contact),
    path('about_project', views.about_project),
    path('test', views.test)
]
