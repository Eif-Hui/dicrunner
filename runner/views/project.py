# -*- coding: utf-8 -*-
# @Time    : 2021/3/20 8:30 上午
# @Author  : Hui
# @File    : project.py


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from runner.models import Project
from runner.serializers import ProjectSerializer
from runner.tools import runResponse as rep


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminUser]


class ProjectView(APIView):

    def post(self,request):
        """
        项目新增
        :param request:
        :return:
        """
        try:
            project_name = request.data["name"]
            #env_config = request.data["envConfig"]
        except KeyError:
            return Response(rep.KEY_MISS)
        if Project.objects.filter(name=project_name).first():
            return Response(rep.REGISTER_PROJECT_EXIST)
        serializer = ProjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(rep.REGISTER_SUCCESS)
        else:
            return Response(rep.SYSTEM_ERROR)


    def put(self,request):
        """
        项目编辑
        :param request:
        :return:
        """
        project_id = request.GET.get("id")
        projects_info = Project.objects.get(id = project_id)
        rep.REGISTER_SUCCESS["projectInfo"] = {
            "id":projects_info.id,
            "name":projects_info.name,
            "env_config":projects_info.env_config
        }
        return Response(rep.REGISTER_SUCCESS)

    def get(self,request):
        """
        :param request:
        :return: 根据项目id信息
        """
        project_id = request.GET.get("id")
        projects_info = Project.objects.get(id = project_id)
        rep.REGISTER_SUCCESS["projectInfo"] = {
            "id":projects_info.id,
            "name":projects_info.name,
            "env_config":projects_info.env_config
        }
        return Response(rep.REGISTER_SUCCESS)


@api_view(['GET'])
def project_env(request, *args, **kwargs):
    data = {"projectEnvList": [], "curProjectEnv": {}}
    projects = Project.objects.all()
    if not projects:
        return Response(data, status=status.HTTP_200_OK)
    for project in projects:
        data["projectEnvList"].append({"projectId": str(project.id),
                                       "projectName": project.name,
                                       "envList": project.env_config.replace(" ", "").split(",")})
    data["curProjectEnv"] = {"curProjectId": str(projects[0].id),
                             "curProjectName": projects[0].name,
                             "curEnvName": projects[0].env_config.replace(" ", "").split(",")[0]}
    return Response(data, status=status.HTTP_200_OK)