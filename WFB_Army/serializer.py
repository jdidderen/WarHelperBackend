from rest_framework import serializers
from .models import Army
from WFB_Stratagem.serializer import StratagemSerializer

class ArmySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')
    stratagem_ids = StratagemSerializer(many=True)

    class Meta:
        model = Army
        fields = ('id',
                  'name','image_url','stratagem_ids')

    def get_image_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.get_image_url())