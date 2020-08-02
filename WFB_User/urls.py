from django.conf.urls import url
from . import api

urlpatterns = [
    url(r'^$', api.userList),
    url(r'^(?P<id>[0-9]+)$', api.userDetail),
]