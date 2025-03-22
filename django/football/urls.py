from django.urls import path
from . import views

urlpatterns = [
    path('score/', views.football_score, name='football_score'),
    path('players/', views.football_players, name='football_players'),
]