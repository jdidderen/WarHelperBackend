from rest_framework import serializers
from .models import Objective,ObjectiveType

class ObjectiveTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ObjectiveType
        fields = ('id',
                  'name')

class ObjectiveSerializer(serializers.ModelSerializer):
    type_id = ObjectiveTypeSerializer()
    description_url = serializers.SerializerMethodField('get_description_url')

    class Meta:
        model = Objective
        fields = ('id',
                  'name','description_url','type_id')

    def get_description_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.get_description_url())