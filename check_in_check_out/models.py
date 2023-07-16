from django.db import models
from django.contrib.auth.models import User

class Check_in (models.Model):
    date_time = models.DateTimeField()
    lateness = models.BooleanField()
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s %s"%(self.owner.first_name, self.date_time)


class Check_out (models.Model):
    date_time = models.DateTimeField()
    lateness = models.BooleanField()
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s"%(self.owner.first_name, self.date_time)

