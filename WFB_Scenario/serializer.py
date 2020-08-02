from rest_framework import serializers
from .models import Scenario,ScenarioType

class ScenarioTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScenarioType
        fields = ('id',
                  'name','point_limit')

class ScenarioSerializer(serializers.ModelSerializer):
    type_id = ScenarioTypeSerializer()
    rules_url = serializers.SerializerMethodField('get_rules_url')
    deployment_url = serializers.SerializerMethodField('get_deployment_url')

    class Meta:
        model = Scenario
        fields = ('id',
                  'name','type_id','rules_url','deployment_url')

    def get_rules_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.get_rules_url())

    def get_deployment_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.get_deployment_url())