from rest_framework import serializers
from .models import PersonalObjective


class PersonalObjectiveSerializer(serializers.ModelSerializer):
    player = serializers.SerializerMethodField('get_player',read_only=True)



    class Meta:
        model = PersonalObjective
        fields = ('id','date',
                  'name','description','player_id','player')

    def get_player(self, obj):
        if obj.player_id:
            return obj.player_id.username
        else:
            return ''