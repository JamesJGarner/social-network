from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    
    from_user = models.ForeignKey(
        User
        )
    
    to_user = models.ForeignKey(
        User,
        related_name='to_user'
        )

    text = models.CharField(
        max_length=100,
        )
    
    date = models.DateTimeField(
        null=True,
        )
    
    read = models.BooleanField(
        default=False,
        )
    
    class Meta:
        ordering = ['date']


class Reply(models.Model):

    message = models.ForeignKey(
        Message
        )

    from_user = models.ForeignKey(
        User
        )

    text = models.CharField(
        max_length=100,
        )
    
    date = models.DateTimeField(
        null=True,
        )
    
    read = models.BooleanField(
        default=False,
        )