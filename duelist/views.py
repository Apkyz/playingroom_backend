
from duelist.models import Deck, Duelist
from duelist.serializers import DeckSerializer, DuelistSerializer
from rest_framework import viewsets

class DeckViewSet(viewsets.ModelViewSet):

    serializer_class = DeckSerializer
    queryset = Deck.objects.all()
    
class DuelistViewSet(viewsets.ModelViewSet):

    serializer_class = DuelistSerializer
    queryset = Duelist.objects.all()