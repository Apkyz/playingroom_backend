from rest_framework import serializers

from duelist.models import Deck


class DeckSerializer(serializers.ModelSerializer):
        class Meta :
            model = Deck
            fields = '__all__'