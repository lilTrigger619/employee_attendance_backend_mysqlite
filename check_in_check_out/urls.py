from django.urls import path
from .views import Get_all_logs, Get_week_logs, Get_month_logs, Get_all_check_out_logs


urlpatterns = [
    path("", Get_all_logs.as_view()),
    path("week/", Get_week_logs.as_view()),
    path("month/", Get_month_logs.as_view()),
    path("check_out/", Get_all_check_out_logs.as_view()),
]
