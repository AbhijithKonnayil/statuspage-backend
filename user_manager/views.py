from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView
from django.utils.translation import gettext_lazy as _
from rest_framework import status, viewsets
from rest_framework.exceptions import NotAcceptable, ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response

from .models import Organization, Team, User
from .serializers import (LoginSerializer_, OrganizationSerializer,
                          RegisterSerializer_, TeamSerializer, UserSerializer)


class UserResponseMixin:
    def get_response_data(self, user):
        return {'token': user.auth_token.key,
                'id': user.id,
                'username': user.username,
                'organization': user.organization.name,
                }

    def get_response_(self):
        return Response(self.get_response_data(), status=status.HTTP_200_OK)


class RegisterView_(
    UserResponseMixin,
    RegisterView,
):
    serializer_class = RegisterSerializer_


class LoginView_(
    UserResponseMixin,
    LoginView
):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer_

    def post(self, request, *args, **kwargs):
        setattr(request._request, 'data', request.data)
        return super().post(request, *args, **kwargs)


class LogoutView_(LogoutView):
    permission_classes = [IsAuthenticated]


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
