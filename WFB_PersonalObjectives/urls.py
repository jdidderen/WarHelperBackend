from django.conf.urls import url
from . import api

urlpatterns = [
    url(r'^$', api.personalObjectiveList),
    url(r'^create$', api.personalObjectiveCreate),
    url(r'^(?P<id>[0-9]+)$', api.personalObjectiveDetail),
    url(r'^update/(?P<id>[0-9]+)$', api.personalObjectiveUpdate),
    url(r'^delete/(?P<id>[0-9]+)$', api.personalObjectiveDelete),
]