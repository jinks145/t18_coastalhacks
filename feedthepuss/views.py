from feedthepuss.services import UserService
from feedthepuss.models import User, Pet, Report
from feedthepuss.serializers import AddPetSerializer, LoginSerializer, SignUpSerializer, AddReportSerializer
from rest_framework import generics, permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


class LoginView(generics.GenericAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = LoginSerializer


class SignUpView(generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = SignUpSerializer


class PetView(generics.CreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = AddPetSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]


class AddReportView(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = AddReportSerializer

    #TODO: limit permission  to author
    permission_classes = [
        permissions.IsAuthenticated,
    ]

class ManageReportView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = AddReportSerializer

    permission_classes = [
        permissions.IsAuthenticated,
    ]

@swagger_auto_schema(
    method="POST",
)
@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def reportSuccess(request):
    UserService.reportSuccess(request.user)
    return Response(status=status.HTTP_202_ACCEPTED)
