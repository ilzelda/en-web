from django.urls import path
from introduce import views

urlpatterns = [
    path('', views.showHome, name='home'), ##url이 '~introduce/'일때
    path('createtodo/', views.createTodo, name='createtodo'),
]
