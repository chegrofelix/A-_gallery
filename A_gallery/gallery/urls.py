from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='galley-home'),
    path('', views.about, name='galley-about'),
]