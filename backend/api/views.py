from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import HighScore
from .serializers import HighScoreSerializer


@api_view(["GET"])
def health(request):
    return Response({"message": "Server is up!"})


@api_view(["GET", "POST"])
def highscores(request):
    """
    List top highscores or submit a new score.
    GET: returns top 10 scores.
    POST: accepts {player_name, score, level}.
    """
    if request.method == "GET":
        qs = HighScore.objects.all().order_by("-score", "created_at")[:10]
        return Response(HighScoreSerializer(qs, many=True).data)

    serializer = HighScoreSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    hs = serializer.save()
    return Response(HighScoreSerializer(hs).data, status=status.HTTP_201_CREATED)
