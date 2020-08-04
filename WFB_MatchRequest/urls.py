from django.conf.urls import url
from . import api

urlpatterns = [
    url(r'^$', api.matchRequestList),
    url(r'^create$', api.matchRequestCreate),
    url(r'^(?P<id>[0-9]+)$', api.matchRequestDetail),
    url(r'^update/(?P<id>[0-9]+)$', api.matchRequestUpdate),
    url(r'^delete/(?P<id>[0-9]+)$', api.matchRequestDelete),
]