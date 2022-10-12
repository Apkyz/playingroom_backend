
from duelist.models import Deck
from duelist.serializers import DeckSerializer
from rest_framework import viewsets

class DeckViewSet(viewsets.ModelViewSet):

    serializer_class = DeckSerializer
    queryset = Deck.objects.all()