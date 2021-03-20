# -*- coding: utf-8 -*-
# @Time    : 2021/3/20 8:30 上午
# @Author  : Hui
# @File    : envvar.py
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from runner.models import EnvVar
from runner.serializers import EnvVarSerializer


class EnvVarViewSet(ModelViewSet):
    queryset = EnvVar.objects.all()
    serializer_class = EnvVarSerializer

    def list(self, request, *args, **kwargs):
        project_id = request.GET.get("curProjectId")
        env_name = request.GET.get("curEnvName")
        queryset = EnvVar.objects.filter(Q(project_id=project_id) & Q(env_name=env_name))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)