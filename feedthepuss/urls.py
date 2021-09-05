from django.urls import path
from feedthepuss import views
# TODO: need to refractor the urlpatterns and maybe switch to viewsets?
urlpatterns = [
    path("users/signup", views.SignUpView.as_view()),
    path("pet/create", views.PetView.as_view()),
    path("reportSuccess", views.reportSuccess),
    path("reports", views.ListUserReportView.as_view()),
    path("reports/add", views.AddReportView.as_view()),
    path("reports/update/name=title", views.AddReportView.as_view()),
]
