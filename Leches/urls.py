from django.urls import path
from . import views
from .views import update,delete

urlpatterns = [
    path('', views.index, name='index'),
    path('crud', views.crud, name='crud'),
    path('list', views.list, name='list'),
    path('new', views.new, name='new'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
    path('carrusel', views.carrusel, name='carrusel'),
]
