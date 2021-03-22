from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='gallery-home'),
    path('', views.about, name='gallery-about'),
]