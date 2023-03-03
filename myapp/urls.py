from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.home, name="Inicio"),
    path('actividades', views.actividades, name="Actividades"),
    path('seguimiento', views.seguimiento, name="Seguimiento"),   
]