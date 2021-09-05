from feedthepuss.models import Report
from django_filters import rest_framework as filters


class ReportFilter(filters.FilterSet):
    class Meta:
        model = Report
        fields = ("is_success", "title")
