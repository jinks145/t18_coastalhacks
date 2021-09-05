from django.urls import path
from feedthepuss import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"reports", views.ReportView, basename="report")
urlpatterns = [
    path("users/signup", views.SignUpView.as_view()),
    path("users/<int:pk>/profile", views.ProfileView.as_view()),
    path("pet", views.PetView.as_view()),
] + router.urls
