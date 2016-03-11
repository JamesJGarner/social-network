from django.conf.urls import patterns, include, url
from .views import ListPost, CreatePost, DetailPost, DeletePost

urlpatterns = [
    url(r'^$', ListPost.as_view(), name="list_post"),
    url(r'^post/$', CreatePost.as_view(), name="create_post"),
    url(r'^posts/(?P<pk>\d+)/$', DetailPost.as_view(), name="detail_post"),
    url(r'^posts/(?P<pk>\d+)/delete/$', DeletePost.as_view(), name='delete_post'),
]
