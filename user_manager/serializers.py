from dj_rest_auth.registration.serializers import (RegisterSerializer,
                                                   SocialLoginSerializer)
from dj_rest_auth.serializers import (LoginSerializer,
                                      PasswordResetConfirmSerializer)
from rest_framework import serializers

from .models import Organization, Team, User


class RegisterSerializer_(RegisterSerializer):
    organization = serializers.CharField(max_length=25)
    pass

    def save(self, request):
        user = super().save(request)
        org_name = self.validated_data.get('organization')
        org = Organization.objects.create(name=org_name)
        user.organization = org
        user.role = "Admin"
        user.save()
        return user


class LoginSerializer_(LoginSerializer):
    email = None


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'organization',
                  'teams', 'role', 'created_at', 'updated_at']
