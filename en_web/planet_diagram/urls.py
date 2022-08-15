from django.urls import path
from planet_diagram import views

urlpatterns = [
    path('', views.showUniverse, name='universe'), 
    path('createplanet/', views.createPlanet, name='createplanet'),
]
