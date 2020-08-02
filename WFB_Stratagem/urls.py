from django.conf.urls import url
from . import api

urlpatterns = [
    url(r'^$', api.stratagemList),
    url(r'^phase$', api.stratagemPhaseList),
    url(r'^create$', api.stratagemCreate),
    url(r'^(?P<id>[0-9]+)$', api.stratagemDetail),
    url(r'^update/(?P<id>[0-9]+)$', api.stratagemUpdate),
    url(r'^delete/(?P<id>[0-9]+)$', api.stratagemDelete),
]