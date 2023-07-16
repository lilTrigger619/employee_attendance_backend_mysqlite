from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.schemas.coreapi import serializers
from .serializers import Check_serializer, User_serializer
from .models import Check_in, Check_out
from datetime import datetime, timedelta
from django.db.models import Q 


# list all logs for all users 
class Get_all_logs(ListAPIView):
    serializer_class = Check_serializer
    permission_classes = [IsAuthenticated]
    queryset = Check_in.objects.all()

# list all logs for checkout all users
class Get_all_check_out_logs(ListAPIView):
    serializer_class = Check_serializer
    permission_classes = [IsAuthenticated]
    queryset = Check_out.objects.all()

# list all logs of all users for a week
class Get_week_logs(ListAPIView):
    serializer_class = Check_serializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        current_date = datetime.now().date()
        start_date = current_date - timedelta(days=current_date.weekday())
        end_date = start_date + timedelta(days=4)
        return Check_in.objects.filter(Q(date_time__range=[start_date, end_date])) 

# list all logs of all users for a month
class Get_month_logs(ListAPIView):
    serializer_class = Check_serializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        current_date = datetime.now().date()
        start_date = datetime(current_date.year, current_date.month, 1)
        end_date = start_date.replace(day=1, month=current_date.month+1) - timedelta(days=1)
        return Check_in.objects.filter(Q(date_time__range=[start_date, end_date])) 

# create a log when the user check's in.
class Create_a_log(CreateAPIView):
    serializer_class = Check_serializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        obj = {**request.data, "owner":request.user.id}
        _ser = self.get_serializer(data=obj)
        if _ser.is_valid():
            _ser.save()
            return Response(_ser.data, status=HTTP_200_OK)
        return Response(_ser.errors, status=HTTP_400_BAD_REQUEST)
