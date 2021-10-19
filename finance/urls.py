from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('listed_companies/', views.listed_companies, name='Listed_Companies')
]