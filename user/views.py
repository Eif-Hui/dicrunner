from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from user.common.tokenMiddleware import *
from rest_framework.response import Response
from rest_framework.views import APIView
from user.common import response
from user import models
from user import serializers
import logging
from django.contrib.auth.hashers import make_password, check_password

logger = logging.getLogger('DicRunner')


class RegisterView(APIView):

    authentication_classes = ()
    permission_classes = ()

    """
    注册:{
        "user": "test"
        "password": "abcd1234"
        "email": "1@1.com"
    }
    """
    def post(self, request):

        try:
            username = request.data["username"]
            password = request.data["password"]
            email = request.data["email"]
        except KeyError:
            return Response(response.KEY_MISS)

        if models.UserInfo.objects.filter(username=username).first():
            return Response(response.REGISTER_USERNAME_EXIST)

        if models.UserInfo.objects.filter(email=email).first():
            return Response(response.REGISTER_EMAIL_EXIST)

        request.data["password"] = make_password(password)

        serializer = serializers.UserInfoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(response.REGISTER_SUCCESS)
        else:
            return Response(response.SYSTEM_ERROR)



class LoginView(APIView):
    """
    登陆视图，用户名与密码匹配返回token
    """
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        """
        用户名密码一致返回token
        {
            "username": "test",
            "password": "abcd1234"
        }
        """
        try:
            username = request.data["username"]
            password = request.data["password"]
        except KeyError:
            return Response(response.KEY_MISS)

        user = models.UserInfo.objects.filter(username=username).first()

        if not user:
            return Response(response.USER_NOT_EXISTS)

        if not check_password(password, user.password):
            return Response(response.LOGIN_FAILED)

        token = generate_token(username)

        try:
            models.UserToken.objects.update_or_create(user=user, defaults={"token": token})
        except ObjectDoesNotExist:
            return Response(response.SYSTEM_ERROR)
        else:
            response.LOGIN_SUCCESS["token"] = token
            response.LOGIN_SUCCESS["user"] = username
            return Response(response.LOGIN_SUCCESS)
