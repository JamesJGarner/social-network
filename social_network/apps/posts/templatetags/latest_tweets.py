from social_network.apps.posts.models import Post
from social_network.apps.userprofiles.models import UserProfile
from django.db.models import Sum
from django.contrib.auth.models import User
from django import template

register = template.Library()

@register.inclusion_tag("site/latest_tweets.html", takes_context=True)
def latest_tweets(context):
    latest_tweets = SingleTweet.objects.filter(
        user__in=[profile.user.pk for profile in context['user'].profile.follows.all()] + [context['user'].pk]
    ).order_by('-date')
    context['latest_tweets'] = latest_tweets
    return context

#need to fix following, for some reason i don't know what the issue it haha
