from django.urls import path
from . import views

urlpatterns = [
    path('', views.view, name='view'),
    path('<int:idlist>', views.todo, name='list'),
    # path('<int:idlist>/<int:iditem>', views.getItem, name='getItem'),
    # path('add/<str:name>', views.addList, name='addList'),
    # path('<int:idlist>/add/<str:text>', views.addItem, name='addItem'),
    # path('del/<int:idlist>', views.delList, name='delList'),
    path('<int:idlist>/edit', views.edit, name='edit'),
    path('create/', views.create, name='create'),
    ]