from rest_framework import generics
from .serializers import TeamSerializer
from .models import Team


# Create your views here.
class TeamList(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

