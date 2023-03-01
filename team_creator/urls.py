from django.urls import path
from team_creator import views

urlpatterns = [
    path('GameSet', views.team_players, name='TeamForm'),
    path('game_play/',views.team_view),
    path('shotForm/<int:pk>', views.shotForm, name="shotForm"),
    path('GameReset/', views.GameReset, name="GameReset"),
    path('', views.GameView, name="GameView"),
    path('undo', views.Undo, name="Undo"),
    
    
]