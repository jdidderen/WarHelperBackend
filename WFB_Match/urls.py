from django.conf.urls import url
from . import api

urlpatterns = [
    url(r'^$', api.matchList),
    url(r'^create$', api.matchCreate),
    url(r'^lastfive$', api.matchListLastFive),
    url(r'^update/(?P<id>[0-9]+)$', api.matchUpdate),
    url(r'^delete/(?P<id>[0-9]+)$', api.matchDelete),
]