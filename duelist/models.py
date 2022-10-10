from django.db import models


class Deck(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Duelist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cosy = models.CharField(max_length=20)
    decks = models.ManyToManyField(Deck, related_name='players')
    
    def __str__(self):
        return self.first_name + " " + self.last_name
