from rest_framework import serializers
from .models import Stratagem,StratagemPhase

class StratagemSerializer(serializers.ModelSerializer):
    army = serializers.SerializerMethodField('get_army')


    class Meta:
        model = Stratagem
        fields = ('id',
                  'name','description','cost','type','army_id','phase_id','army')

    def get_army(self, obj):
        if obj.army_id:
            return obj.army_id.name
        else:
            return ''

class StratagemPhaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = StratagemPhase
        fields = ('id',
                  'name')
