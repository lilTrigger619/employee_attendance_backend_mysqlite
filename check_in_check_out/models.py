from django.db import models
from django.contrib.auth.models import User
from admin_settings.models import Admin_configs

class Check_in (models.Model):
    date_time = models.DateTimeField()
    #lateness = models.BooleanField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def lateness (self):
        return Admin_configs.objects.first().show_up_time.time() < self.date_time.time()

    def __str__(self):
        return "%s %s"%(self.owner.first_name, self.date_time)


class Check_out (models.Model):
    date_time = models.DateTimeField()
    # lateness = models.BooleanField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def lateness (self):
        return Admin_configs.objects.first().show_up_time.time() < self.date_time.time()

    def __str__(self):
        return "%s %s"%(self.owner.first_name, self.date_time)

