from django.conf.urls import url
from . import api

urlpatterns = [
    url(r'^$', api.matchList),
    url(r'^my/(?P<user_id>[0-9]+)$', api.myMatchList),
    url(r'^create$', api.matchCreate),
    url(r'^line/create$', api.matchCreateLine),
    url(r'^lastfive$', api.matchListLastFive),
    url(r'^(?P<id>[0-9]+)$', api.matchDetail),
    url(r'^update/(?P<id>[0-9]+)$', api.matchUpdate),
    url(r'^delete/(?P<id>[0-9]+)$', api.matchDelete),
]