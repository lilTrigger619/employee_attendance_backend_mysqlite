from django.db import models

class Admin_configs(models.Model):
    auto_check_out = models.BooleanField()
    location_check = models.BooleanField()
    show_up_time = models.DateTimeField()



