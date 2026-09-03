from django.urls import path
from . import views

app_name = 'parques'

urlpatterns = [
    path('', views.home, name='home'),
    path('parques/', views.parques_list, name='parques_list'),
    path('parques/<int:park_id>/', views.parque_detail, name='parque_detail'),
    path('actividades/', views.actividades, name='actividades'),
    path('contacto/', views.contacto, name='contacto'),
]
