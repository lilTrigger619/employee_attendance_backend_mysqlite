from rest_framework import serializers
from .models import Admin_configs

class Admin_config_serializer(serializers.ModelSerializer):
    class Meta:
        model = Admin_configs
        fields = "__all__"
