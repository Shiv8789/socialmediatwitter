
from django.urls import path
from . import views

#application urls

urlpatterns = [
    path('', views.home, name='home'),
    path('mytweet/', views.mytweet, name='mytweet'),
    path('tweethandle/', views.tweethandle, name='tweethandle'),
    path('updatetweet/<int:id>', views.updatetweet, name='updatetweet'),
    path('deletetweet/<int:id>', views.deletetweet, name='deletetweet'),
    path('about/', views.about, name='about'),
    
]