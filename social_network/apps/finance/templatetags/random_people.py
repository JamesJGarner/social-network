from django.contrib.auth.models import User
from django.db.models import Sum

from django import template

register = template.Library()

@register.inclusion_tag("site/random_people.html")
def random_people():
    random_people = User.objects.all().order_by('?')[:20]
    return {
        "random_people": random_people
    }
