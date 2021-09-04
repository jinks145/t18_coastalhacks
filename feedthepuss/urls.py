from django.urls import path
from feedthepuss import views

urlpatterns = [
    path("users/signup", views.SignUpView.as_view()),
    path("pet/create", views.PetView.as_view()),
    path("reportSuccess", views.reportSuccess),
]
