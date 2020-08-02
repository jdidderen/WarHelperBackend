from rest_framework import serializers
from .models import Unit

class UnitSerializer(serializers.ModelSerializer):
    unit_type = serializers.SerializerMethodField('get_unit_type')
    army_name = serializers.SerializerMethodField('get_army_name')

    class Meta:
        model = Unit
        fields = ('id',
                  'name','unit_type','army_name')

    def get_unit_type(self, obj):
        if obj.unit_type_id:
            return obj.unit_type_id.name
        else:
            return ''

    def get_army_name(self, obj):
        if obj.army_id:
            return obj.army_id.name
        else:
            return ''
