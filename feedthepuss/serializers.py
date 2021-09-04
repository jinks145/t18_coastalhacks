from rest_framework import serializers
from feedthepuss.models import Pet, User
from django.contrib.auth.hashers import make_password


class SignUpSerializer(serializers.ModelSerializer):
    def validate_password(self, value):
        return make_password(value)

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email", "password", "age", "sex")


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password")


class AddPetSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Pet
        fields = ("id", "user", "name")
