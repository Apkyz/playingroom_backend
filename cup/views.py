from cup.models import Championship, Match
from cup.serializers import ChampionshipSerializer, MatchSerializer
from rest_framework import viewsets


class ChampionshipViewSet(viewsets.ModelViewSet):
    serializer_class = ChampionshipSerializer
    queryset = Championship.objects.all()
    
class MatchViewSet(viewsets.ModelViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()