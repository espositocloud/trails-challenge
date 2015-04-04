from rest_framework import serializers

from .models import Group, Technique, Patrol, Test


class TechniqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Technique
        depth = 1
        fields = (
            'id',
            'name',
            'patrols_number',
            'last_patrol',
            'check_condition',
        )


class TestSerializer(serializers.ModelSerializer):
    technique = serializers.PrimaryKeyRelatedField(queryset=Technique.objects.all())
    patrol = serializers.PrimaryKeyRelatedField(queryset=Patrol.objects.all())

    class Meta:
        model = Test
        fields = (
            'patrol',
            'technique',
            'technique_score',
            'style_score',
            'created_date_hms',
            'user',
        )
        read_only_fields = ('technique', 'patrol')


class PatrolSerializer(serializers.ModelSerializer):
    group = serializers.StringRelatedField()
    tests = TestSerializer(many=True)

    class Meta:
        model = Patrol
        depth = 1
        fields = (
            'id',
            'group',
            'name',
            'hour_condition',
            'check_condition',
            'conditions',
            'technique_score',
            'style_score',
            'total_score',
            'ranking',
            'avg_technique_score',
            'avg_style_score',
            'tests',
        )


class GroupSerializer(serializers.ModelSerializer):
    patrols = PatrolSerializer(many=True)

    class Meta:
        model = Group
        depth = 1
        fields = (
            'id',
            'name',
            'patrols',
        )
