from django.urls import path
from planet_diagram import views

urlpatterns = [
    path('', views.showUniverse, name='universe'), 
    path('createplanet/', views.createPlanet, name='createplanet'),
    path('planetdetail/<int:planet_id>', views.showPlanetDetail, name='planetdetail'),
    path('createcomment/<int:planet_id>', views.createComment, name='createcomment'),

]
