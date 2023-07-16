from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import Admin_config_serializer
from .models import Admin_configs
from check_in_check_out.serializers import User_serializer
from django.contrib.auth.models import User

# we only create one instance of the settings model and update it 
# after.
class Update_retrieve_admin_settings(RetrieveUpdateAPIView):
    serializer_class = Admin_config_serializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Admin_configs.objects.first()

class Create_employee(CreateAPIView):
    serializer_class=User_serializer
    permission_classes=[IsAuthenticated]
    queryset = User.objects.all()
