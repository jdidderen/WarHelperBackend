from django.conf.urls import url
from . import api

urlpatterns = [
    url(r'^$', api.armyList),
    url(r'^create$', api.armyCreate),
    url(r'^(?P<id>[0-9]+)$', api.armyDetail),
    url(r'^update/(?P<id>[0-9]+)$', api.armyUpdate),
    url(r'^delete/(?P<id>[0-9]+)$', api.armyDelete),
]