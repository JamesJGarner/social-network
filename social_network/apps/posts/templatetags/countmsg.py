from social_network.apps.communication.models import Message
from social_network.apps.userprofiles.models import UserProfile
from django.db.models import Sum
from django.contrib.auth.models import User
from django import template

register = template.Library()

@register.inclusion_tag("site/countmsg.html", takes_context=True)
def countmsg(context):
    request = context['request']
    countmsg = Message.objects.filter(
        to_user=request.user.id, read=False
    ).count
    context['countmsg'] = countmsg
    return context

