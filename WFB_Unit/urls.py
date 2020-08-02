from django.conf.urls import url
from . import api

urlpatterns = [
    url(r'^$', api.unitList),
    url(r'^create$', api.unitCreate),
    url(r'^(?P<id>[0-9]+)$', api.unitDetail),
    url(r'^update/(?P<id>[0-9]+)$', api.unitUpdate),
    url(r'^delete/(?P<id>[0-9]+)$', api.unitDelete),
]
