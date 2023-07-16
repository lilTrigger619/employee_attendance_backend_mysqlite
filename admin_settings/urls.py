from django.urls import path
from .views import Update_retrieve_admin_settings

urlpatterns = [
        path("", Update_retrieve_admin_settings.as_view()),
    ]
