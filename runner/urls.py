"""dicrunner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user import views
from runner.views import project, envvar, fixture,case

urlpatterns = [
    path(r"projects", project.ProjectView.as_view()),
    path(r"projects/<int:pk>", project.ProjectViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "delete": "destroy"
    })),
    path(r"projects/env", project.project_env),

    path(r"envvars", envvar.EnvVarViewSet.as_view({
        "get": "list",
        "post": "create"
    })),
    path(r"envvars/<int:pk>", envvar.EnvVarViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "delete": "destroy"
    })),

    path(r"fixtures", fixture.FixtureViewSet.as_view({
        "get": "list",
        "post": "create"
    })),
    path(r"fixtures/<int:pk>", fixture.FixtureViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "delete": "destroy"
    })),
    path(r"cases", case.CaseViewSet.as_view({
        "get": "list",
        "post": "create"
    })),
    path(r"cases/<int:pk>", case.CaseViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "delete": "destroy"
    })),
    path(r"cases/<int:pk>/result", case.case_result),
    path(r"cases/<int:pk>/copy", case.copy_case),

]
