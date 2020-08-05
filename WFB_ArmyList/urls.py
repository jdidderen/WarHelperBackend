from django.conf.urls import url
from . import api

urlpatterns = [
    url(r'^$', api.armyListList),
    url(r'^create$', api.armyListCreate),
    url(r'^(?P<id>[0-9]+)$', api.armyListDetail),
    url(r'^update/(?P<id>[0-9]+)$', api.armyListUpdate),
    url(r'^delete/(?P<id>[0-9]+)$', api.armyListDelete),
]