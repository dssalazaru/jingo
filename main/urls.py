from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dssu/', views.dssu, name='dssu'),
    path('dssu/test/', views.test, name='test'),
    ]