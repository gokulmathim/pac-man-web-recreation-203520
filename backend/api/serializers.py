from rest_framework import serializers
from .models import HighScore


class HighScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = HighScore
        fields = ["id", "player_name", "score", "level", "created_at"]
        read_only_fields = ["id", "created_at"]
