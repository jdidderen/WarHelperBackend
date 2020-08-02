from rest_framework import serializers
from .models import Army
from WFB_Stratagem.serializer import StratagemSerializer

class ArmySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')
    units = serializers.SerializerMethodField('get_unit_per_type')
    stratagem_ids = StratagemSerializer(many=True)

    class Meta:
        model = Army
        fields = ('id',
                  'name','image_url','units','stratagem_ids')

    def get_image_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.get_image_url())

    def get_unit_per_type(self, obj):
        types = obj.unit_ids.values_list('unit_type_id',flat=True).distinct()
        arr = []
        if types:
            for unit_type in types:
                units = obj.unit_ids.filter(unit_type_id=unit_type,army_id=obj.id)
                if units:
                    arr.append({'type':units[0].unit_type_id.name,'units':list(units.values_list('name', flat=True).distinct())})
        return arr