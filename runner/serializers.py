# -*- coding: utf-8 -*-
# @Time    : 2021/3/20 8:26 上午
# @Author  : Hui
# @File    : serializers.py


from rest_framework import serializers

from runner.models import Project, EnvVar, Fixture


class ProjectSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)
    envConfig = serializers.CharField(source="env_config")

    class Meta:
        model = Project
        fields = ["id", "name", "envConfig"]


class EnvVarSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)
    curProjectId = serializers.CharField(source="project_id")
    curEnvName = serializers.CharField(source="env_name")

    class Meta:
        model = EnvVar
        fields = ["id", "name", "value", "desc", "curProjectId", "curEnvName"]


class FixtureSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)
    creatorNickname = serializers.CharField(source="creator_nickname")
    curProjectId = serializers.CharField(source="project_id")

    class Meta:
        model = Fixture
        fields = ["id", "name", "desc", "code", "creatorNickname", "curProjectId"]