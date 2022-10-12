from rest_framework import serializers

from duelist.models import Deck, Duelist


class DeckSerializer(serializers.ModelSerializer):
        class Meta :
            model = Deck
            fields = '__all__'
            
class DuelistSerializer(serializers.ModelSerializer):
        class Meta :
            model = Duelist
            fields = '__all__'