from django.db import models
from django.conf import settings
from django.utils.timezone import activate

from django.contrib.auth.models import User

# Create your models here.


USER = settings.AUTH_USER_MODEL

class Victim(models.Model):

    user = models.ForeignKey(USER, default=1, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    address = models.TextField(max_length=1000, null=True)
    total_adults = models.PositiveIntegerField(null=True, default = 1)
    total_children = models.PositiveIntegerField(null=True, default=0)
    total_elderly = models.PositiveIntegerField(null=True, default = 0)
    lat = models.FloatField()
    lon = models.FloatField()                   
    number = models.IntegerField()              # User's Number
    number_2 = models.IntegerField()            # Victim's Number, need not be same as Users.
    roof = models.BooleanField(null=True, default=False)   # Availability of Rooftop for airlift
    info = models.TextField(null=True, max_length=5000)                   # Extra info to aid rescue team.
    inside_dz = models.BooleanField(null=True)
    # situation = models.ForeignKey()
  
class Situation(models.Model):
    
    name = models.TextField(max_length=255)
    c_lat = models.FloatField()                 # Center of Situation
    c_lon = models.FloatField()
    radius = models.IntegerField()              # Radius of Situation
    start_time = models.TimeField(null=True)             # Starting time of Situation
    active = models.BooleanField(default=False)
