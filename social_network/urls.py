from django.conf.urls import include, url
from django.contrib import admin
from social_network import settings
from django.contrib.auth import views as auth_views
from django.conf import settings
from .views import HomepageView, RegisterView
admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', auth_views.login),
    url(r'^logout/$', auth_views.logout),
    url(r'^register/$', RegisterView.as_view(), name="login"),

    url(r'^', include('social_network.apps.userprofiles.urls', namespace="userprofiles")),
    url(r'^', include('social_network.apps.posts.urls', namespace="posts")),
    url(r'^', include('social_network.apps.finance.urls', namespace="finance")),

    #url('^settings/change_password/', auth_views.password_change),
    #url('^settings/password_change/done/', auth_views.password_change_done),
    #url(r"^search/", include("watson.urls", namespace="watson")),
]


#TODO check if needed
if settings.DEBUG == False:
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
    ]
