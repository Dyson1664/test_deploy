from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('john/', views.john, name='john'),
    path('capitals/', views.capitals, name='dave')
]