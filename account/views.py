from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from account.serializers import RegistrationSerializer, ActivationSerializer, LoginSerializer, ChangePasswordSerializer, \
    ForgotPasswordSerializer, User


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = """
            Вы успешно зарегистрировались! 
            Вам отправлено письмо с кодом активации.
            """
            return Response(message)


class ActivationView(APIView):
    def post(self, request):
        serializer = ActivationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.activate()
            return Response('Вы успешно активированы')


# class LoginView(ObtainAuthToken):
#     serializer_class = LoginSerializer

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


# class LogoutView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         user = request.user
#         Token.objects.filter(user=user).delete()
#         return Response('Вы успешно вышли')


class ForgotPasswordView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.create_new_password()
            return Response('Вам на почту выслан новый пароль')


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data,
                                              context={'request': request})
        if serializer.is_valid(raise_exception=True):
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Пароль успешно обновлён',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # return Response('Пароль успешно обновлён')


    #
    # def get_object(self, queryset=None):
    #     obj = self.request.user
    #     return obj
    #
    # def update(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     serializer = self.get_serializer(data=request.data)
    #

            # Check old password

# REST

# 1. Модель client-server
# 2. Отсутствие состояния клиента
# 3. Кеширование
# 4. Единообразие интерфейса
# 5. Система слоёв
# 6. Код по требованию (необязательно)
