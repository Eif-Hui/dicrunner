# -*- coding: utf-8 -*-
# @Time    : 2021/3/20 8:30 上午
# @Author  : Hui
# @File    : fixture.py


from django.db.models import Q
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from runner.models import Fixture
from runner.serializers import FixtureSerializer


class FixtureViewSet(ModelViewSet):
    queryset = Fixture.objects.all()
    serializer_class = FixtureSerializer

    def list(self, request, *args, **kwargs):
        project_id = request.GET.get("curProjectId")
        queryset = Fixture.objects.filter(Q(project_id=project_id))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        fixture_id = kwargs["pk"]
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        request.data["creatorNickname"] = Fixture.objects.get(id=fixture_id).creator_nickname
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
