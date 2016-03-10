from social_network.apps.posts.models import Post
from social_network.apps.userprofiles.models import UserProfile
from django.db.models import Sum
from django.contrib.auth.models import User
from django import template
register = template.Library()


@register.inclusion_tag("site/profile_tweets.html")
def profile_tweets():
    profile_tweets = Post.objects.filter().order_by('-date')[:20]
    return {
        "profile_tweets": profile_tweets
    }
