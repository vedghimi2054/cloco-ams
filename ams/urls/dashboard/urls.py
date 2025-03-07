from django.urls import path

from dashboard.dashboard import DashboardCountView

urlpatterns = [
    path("count", DashboardCountView.as_view(), name="dashboard_count"),
]
