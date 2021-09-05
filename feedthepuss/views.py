from django.http.response import HttpResponse
from feedthepuss.services import UserService
from feedthepuss.models import User, Pet, Report
from feedthepuss.serializers import AddPetSerializer, LoginSerializer, SignUpSerializer, AddReportSerializer, ReportSerializer
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

class ListUserReportView(generics.ListAPIView):

    def get_queryset(self):
        return Report.objects.filter(user= self.request.user)

    serializer_class = AddReportSerializer

    #TODO: limit permission  to author
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

class IsmealsView(generics.ListAPIView):
    
    def get_queryset(self):
        queryset = Report.objects.filter(user = self.request.user, is_meal=True)
        return queryset

    serializer_class = ReportSerializer

    permission_classes = [
        permissions.IsAuthenticated,
    ]

class NotmealLogsView(generics.ListAPIView):

    def get_queryset(self):
        queryset = Report.objects.filter(user = self.request.user, is_meal=False)
        return queryset

    
    serializer_class = ReportSerializer

    permission_classes = [
        permissions.IsAuthenticated,
    ]

class EatLogbyTitleView(generics.RetrieveAPIView):
    def get_queryset(self):
        queryset = Report.objects.filter(user = self.request.user, title=self.kwargs['title'])
        return queryset
    
    
    
    serializer_class = ReportSerializer



    permission_classes = [
        permissions.IsAuthenticated,
    ]

class UpdateLogView(generics.UpdateAPIView):
    def get_queryset(self):
        queryset = Report.objects.filter(user = self.request.user, title=self.kwargs['title'])
        return queryset

    # serializer_class = ReportSerializer
    
    def put(self, request, *args, **kwargs):
        report = self.get_queryset().first()
        Report.objects.delete(title=report.title)
        serializer = AddReportSerializer(report, request.data)
        
        if serializer.is_valid:
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

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
