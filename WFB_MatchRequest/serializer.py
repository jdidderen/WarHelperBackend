from rest_framework import serializers
from .models import MatchRequest


class MatchRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = MatchRequest
        fields = ('id',
                  'name','player_id')