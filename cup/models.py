from django.db import models
from duelist.models import Duelist, Deck


class Championship(models.Model):
    name = models.CharField(max_length=100)
    duelists = models.ManyToManyField(Duelist)
    
class Match(models.Model):
    player1 = models.ForeignKey(Duelist, on_delete=models.CASCADE, related_name='player1')
    deck1 = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='deck1')
    player2 = models.ForeignKey(Duelist, on_delete=models.CASCADE, related_name='player2')
    deck2 = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='deck2')
    winner = models.ForeignKey(Duelist, on_delete=models.CASCADE, related_name='winner')
    status = models.CharField()
    