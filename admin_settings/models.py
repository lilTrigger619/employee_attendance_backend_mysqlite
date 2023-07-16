from django.db import models

class Admin_configs(models.Model):
    auto_check_out = models.BooleanField(default=True)
    location_check = models.BooleanField(default=True)
    show_up_time = models.DateTimeField()



