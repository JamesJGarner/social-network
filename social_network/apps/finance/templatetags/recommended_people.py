from social_network.apps.userprofiles.models import UserProfile
from django.db.models import Sum

from django import template

register = template.Library()

@register.inclusion_tag("site/recommended_people.html")
def recommended_people():
    recommended_people = UserProfile.objects.all().order_by('?')[:4]
    return {
        "recommended_people": recommended_people
    }
