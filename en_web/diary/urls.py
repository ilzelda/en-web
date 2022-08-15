from django.urls import path

from diary import views

urlpatterns = [
    path('', views.showDiaryList, name='diary'),
    path('create/',views.createNewDiary, name='create'),
    path('update/<int:diary_id>',views.updateDiary, name='update'),
   
]
