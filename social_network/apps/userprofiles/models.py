from django.db import models
import watson
from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


class Rank(models.Model):
    
    name = models.CharField(
        max_length=100,
    )
    
    price = models.DecimalField(
        max_digits=100,
        decimal_places=2,
    )
    
    tagline = models.CharField(
        max_length=100,
        null=True,
    )

    buyable = models.BooleanField(
        default=False,
        )
    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    
    user = models.OneToOneField(
        User
    )
    
    color = models.CharField(
        max_length=100,
        blank=True,
    )
    
    name = models.CharField(
        max_length=100,
        blank=True,
    )
    
    picture = models.ImageField(
        upload_to='faces/',
        blank=True,
        default='default.png'
    )
    
    banner = models.ImageField(
        upload_to='faces/',
        blank=True,
    )
    
    url = models.URLField(
        "Website",
         blank=True,
    )
    
    company = models.CharField(
        max_length=50,
        blank=True,
    )
    
    location = models.CharField(
        max_length=100,
        blank=True
    )

    bio = models.TextField(
        blank=True
    )

    follows =  models.ManyToManyField(
        'UserProfile',
        related_name='followed_by',
        blank=True,
    )
    background = models.ImageField(
        upload_to='faces',
        blank=True
    )
    
    balance = models.DecimalField(
        max_digits=100,
        default=0.00,
        decimal_places=2,
         )
    
    rank = models.ForeignKey(
        Rank,
        null=True,
        default=1
    )

    def __unicode__(self):
        return self.name
  

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


#watson.register(UserProfile)

