from rest_framework import serializers
from .models import Check_in 
from django.contrib.auth.models import User


class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")
        extra_kwargs = {"password":{"write_only":True}}

class Check_serializer(serializers.ModelSerializer):
    owner = User_serializer(read_only=True)
    lateness= serializers.CharField(read_only=True)
    class Meta:
        model = Check_in
        fields = "__all__"


