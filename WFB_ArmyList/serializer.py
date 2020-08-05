from rest_framework import serializers
from .models import ArmyList
import bbcode

class ArmyListSerializer(serializers.ModelSerializer):
    player = serializers.SerializerMethodField('get_player',read_only=True)
    army = serializers.SerializerMethodField('get_army',read_only=True)
    descriptionHTML = serializers.SerializerMethodField('get_description_html',read_only=True)

    class Meta:
        model = ArmyList
        fields = ('id','name','description',
                  'player_id','army_id','army','player','descriptionHTML','type')

    def get_player(self, obj):
        if obj.player_id:
            return obj.player_id.username
        else:
            return ''

    def get_army(self, obj):
        if obj.army_id:
            return obj.army_id.name
        else:
            return ''

    def get_description_html(self, obj):
        if obj.description:
            if obj.type == 'aln':
                html = bbcode.render_html(obj.description)
            else:
                html = obj.description
            return html
        else:
            return ''