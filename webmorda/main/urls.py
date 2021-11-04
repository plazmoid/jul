from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('about-us', views.about),
    path('contact', views.contact),
    path('about_project', views.about_project),
    path('test', views.test),
    # регулярное выражение, с которым совпадут url "quiz/любое_количество_цифр", где цифра означает позицию в опроснике
    re_path('^quiz/(?P<pagenum>\d*)', views.quiz)
]
