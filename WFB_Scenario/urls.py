from django.conf.urls import url
from . import api

urlpatterns = [
    url(r'^$', api.scenarioList),
    url(r'^create$', api.scenarioCreate),
    url(r'^(?P<id>[0-9]+)$', api.scenarioDetail),
    url(r'^update/(?P<id>[0-9]+)$', api.scenarioUpdate),
    url(r'^delete/(?P<id>[0-9]+)$', api.scenarioDelete),
]