from rest_framework import serializers
from rest_framework.utils import model_meta
from .models import Match,MatchLine
from WFB_Objective.serializer import ObjectiveSerializer
from WFB_Scenario.serializer import ScenarioSerializer


class MatchLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = MatchLine
        fields = ('id',
                  'match_id', 'player', 'primary_score', 'secondary1_score',
                  'secondary2_score', 'secondary3_score', 'other_score',
                  'cp_used'
                  )


class MatchSerializer(serializers.ModelSerializer):
    line_ids = MatchLineSerializer(many=True,required=False)
    army1 = serializers.SerializerMethodField('get_army1',read_only=True)
    army2 = serializers.SerializerMethodField('get_army2',read_only=True)
    player1 = serializers.SerializerMethodField('get_player1',read_only=True)
    player2 = serializers.SerializerMethodField('get_player2',read_only=True)
    scenario = serializers.SerializerMethodField('get_scenario',read_only=True)
    objective1_p1 = serializers.SerializerMethodField('get_objective1_p1',read_only=True)
    objective2_p1 = serializers.SerializerMethodField('get_objective2_p1',read_only=True)
    objective3_p1 = serializers.SerializerMethodField('get_objective3_p1',read_only=True)
    objective1_p2 = serializers.SerializerMethodField('get_objective1_p2',read_only=True)
    objective2_p2 = serializers.SerializerMethodField('get_objective2_p2',read_only=True)
    objective3_p2 = serializers.SerializerMethodField('get_objective3_p2',read_only=True)

    class Meta:
        model = Match
        fields = (
            'id', 'player1_id', 'player2_id', 'army_p1_id', 'army_p2_id',
            'scenario_id', 'cp_p1', 'cp_p2', 'cp_p1_used_before_battle',
            'cp_p2_used_before_battle', 'date', 'location', 'score_no_details',
            'score_p1', 'score_p2', 'objective1_p1_id', 'objective2_p1_id',
            'objective3_p1_id', 'objective1_p2_id', 'objective2_p2_id', 'objective3_p2_id',
            'line_ids','army1','army2','player1','player2','scenario',
            'objective1_p1','objective2_p1','objective3_p1','objective1_p2','objective2_p2','objective3_p2'
        )
        extra_kwargs = {'score_no_details': {'required': False}}

    def create(self, data):
        line_datas = None
        if 'line_ids' in data:
            line_datas = data.pop('line_ids')
        new_match = Match.objects.create(**data)
        if line_datas:
            for line_data in line_datas:
                MatchLine.objects.create(**line_data, bok=new_match)
        return new_match

    # def _update(self, instance, validated_data):
    #     # drf default implementation
    #     info = model_meta.get_field_info(instance)
    #
    #     for attr, value in validated_data.items():
    #         if attr in info.relations and info.relations[attr].to_many:
    #             field = getattr(instance, attr)
    #             field.set(value)
    #         else:
    #             setattr(instance, attr, value)
    #     instance.save()
    #     return instance
    #
    # def update(self, match, data):
    #     print(data)
    #     line_datas = None
    #     if 'line_ids' in data:
    #         line_datas = data.pop('line_ids')
    #     match = self._update(match, data)
    #     if line_datas:
    #         for line_data in line_datas:
    #             print(line_data)
    #             line = MatchLine.objects.get(id=line_data['id'])
    #             line = self._update(line, line_data)
    #     return match

    def get_army1(self, obj):
        if obj.army_p1_id:
            return obj.army_p1_id.name
        else:
            return ''

    def get_army2(self, obj):
        if obj.army_p2_id:
            return obj.army_p2_id.name
        else:
            return ''

    def get_player1(self, obj):
        if obj.player1_id:
            return obj.player1_id.username
        else:
            return ''

    def get_player2(self, obj):
        if obj.player2_id:
            return obj.player2_id.username
        else:
            return ''

    def get_scenario(self, obj):
        if obj.scenario_id:
            return obj.scenario_id.name + ' | ' + str(obj.scenario_id.type_id.point_limit)
        else:
            return ''

    def get_objective1_p1(self, obj):
        if obj.objective1_p1_id:
            return obj.objective1_p1_id.name
        else:
            return ''

    def get_objective2_p1(self, obj):
        if obj.objective2_p1_id:
            return obj.objective2_p1_id.name
        else:
            return ''

    def get_objective3_p1(self, obj):
        if obj.objective3_p1_id:
            return obj.objective3_p1_id.name
        else:
            return ''

    def get_objective1_p2(self, obj):
        if obj.objective1_p2_id:
            return obj.objective1_p2_id.name
        else:
            return ''

    def get_objective2_p2(self, obj):
        if obj.objective2_p2_id:
            return obj.objective2_p2_id.name
        else:
            return ''

    def get_objective3_p2(self, obj):
        if obj.objective3_p2_id:
            return obj.objective3_p2_id.name
        else:
            return ''

