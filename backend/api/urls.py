from django.urls import path
from .views import health, highscores

urlpatterns = [
    path("health/", health, name="Health"),
    path("highscores/", highscores, name="HighScores"),
]
