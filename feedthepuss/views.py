from feedthepuss.filters import ReportFilter
from django_filters import rest_framework as filters
from Base.serializers import SerializerNone
from feedthepuss.services import UserService
from feedthepuss.models import User, Pet, Report
from feedthepuss.serializers import (
    AddPetSerializer,
    LoginSerializer,
    ProfileSerializerOut,
    ReportSerializerOut,
    ReportSeriliazerIn,
    SignUpSerializer,
)
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


class LoginView(generics.GenericAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = LoginSerializer


class SignUpView(generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = SignUpSerializer


class ProfileView(generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = ProfileSerializerOut


class PetView(generics.CreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = AddPetSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]


class ReportView(viewsets.ModelViewSet):
    http_method_names = ["get", "post"]
    queryset = Report.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    view_serializers = {
        "create": ReportSeriliazerIn,
        "retrieve": ReportSerializerOut,
        "list": ReportSerializerOut,
    }
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ReportFilter

    def get_serializer_class(self):
        return self.view_serializers.get(self.action, SerializerNone)
