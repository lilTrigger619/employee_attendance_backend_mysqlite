from django.urls import path
from .views import Update_retrieve_admin_settings, Create_employee, Get_all_users

urlpatterns = [
        path("", Update_retrieve_admin_settings.as_view()),
        path("register_user/", Create_employee.as_view()),
        path("all_users/", Get_all_users.as_view()),
    ]
