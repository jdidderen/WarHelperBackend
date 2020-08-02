from rest_framework import serializers
from .models import Stratagem,StratagemPhase

class StratagemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stratagem
        fields = ('id',
                  'name','description','cost','type','army_id','phase_id')

class StratagemPhaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = StratagemPhase
        fields = ('id',
                  'name')
