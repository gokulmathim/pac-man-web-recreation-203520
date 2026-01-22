from django.db import models


class HighScore(models.Model):
    """
    HighScore stores top scores for the Pac-Man game.
    """

    player_name = models.CharField(max_length=64)
    score = models.IntegerField()
    level = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-score", "created_at"]

    def __str__(self) -> str:
        return f"{self.player_name}: {self.score} (L{self.level})"
