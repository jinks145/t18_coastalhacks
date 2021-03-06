from rest_framework import serializers
from feedthepuss.models import Pet, User, Report
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


class ProfileSerializerOut(serializers.ModelSerializer):
    class PetSerializerOut(serializers.ModelSerializer):
        class Meta:
            model = Pet
            fields = ("id", "name", "weight")

    pet = PetSerializerOut()

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "age",
            "sex",
            "pet",
        )


class AddPetSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Pet
        fields = ("id", "user", "name")


class ReportSeriliazerIn(serializers.ModelSerializer):

    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Report
        fields = ("uuid", "is_success", "created_by", "title", "body", "mealtime")


class ReportSerializerOut(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ("uuid", "is_success", "title", "body", "mealtime")
