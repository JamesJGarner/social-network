from django.conf.urls import patterns, include, url
from .views import UsersProfile, UserProfilePage
from . import views

urlpatterns = [
    url(r'^settings/$', UserProfilePage.as_view(), name="profile_page"),   
    url(r"^user/(?P<page_slug>[^/]+)/$", UsersProfile.as_view(), name="page_slugs"),
]
