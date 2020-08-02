from django.conf.urls import url
from . import api

urlpatterns = [
    url(r'^$', api.objectiveList),
    url(r'^create$', api.objectiveCreate),
    url(r'^(?P<id>[0-9]+)$', api.objectiveDetail),
    url(r'^update/(?P<id>[0-9]+)$', api.objectiveUpdate),
    url(r'^delete/(?P<id>[0-9]+)$', api.objectiveDelete),
]