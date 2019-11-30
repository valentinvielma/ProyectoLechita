from django.urls import path
from . import views
from .views import update, delete
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('crud', login_required(views.crud, login_url='login'), name='crud'),
    path('list', views.list, name='list'),
    path('new', views.new, name='new'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
    path('carrusel', views.carrusel, name='carrusel'),
    path('logout', views.logout_view, name='logout'),
]
