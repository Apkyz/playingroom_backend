from rest_framework import serializers

from cup.models import Championship, Match


class ChampionshipSerializer(serializers.ModelSerializer):
        class Meta :
            model = Championship
            fields = '__all__'
            
class MatchSerializer(serializers.ModelSerializer):
        class Meta :
            model = Match
            fields = '__all__'