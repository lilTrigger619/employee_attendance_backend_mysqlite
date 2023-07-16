from django.urls import path
from .views import Update_retrieve_admin_settings, Create_employee

urlpatterns = [
        path("", Update_retrieve_admin_settings.as_view()),
        path("register_user/", Create_employee.as_view()),
    ]
