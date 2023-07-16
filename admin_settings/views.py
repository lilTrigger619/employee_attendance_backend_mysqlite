from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import Admin_config_serializer
from .models import Admin_configs

# we only create one instance of the settings model and update it 
# after.
class Update_retrieve_admin_settings(RetrieveUpdateAPIView):
    serializer_class = Admin_config_serializer
    permission_classes = IsAuthenticated

    def get_object(self):
        return Admin_configs.objects.first()
