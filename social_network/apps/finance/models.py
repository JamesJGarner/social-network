from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class GiftCard(models.Model):

    code = models.CharField(
        max_length=16,
        unique=True
        )
   
    worth = models.DecimalField(
        max_digits=100,
        decimal_places=2,
        )
   
    expires = models.DateField(
        null=True,
        )
   
    used = models.BooleanField(
        default=False
        )
   
    def __unicode__(self):
        return self.code

