from django.db import models


class VpnUser(models.Model):
    USER_STATES = ( 
      (0, 'generated'),
      (1, 'paid'),
      (2, 'created'),
      (3, 'expired'),
    )
    address = models.CharField(max_length=144)
    username = models.CharField(max_length=144)
    password = models.CharField(max_length=144)
    state = models.CharField(max_length=2, choices=USER_STATES)
