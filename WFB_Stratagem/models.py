from django.db import models
from rest_framework import serializers
from django.conf import settings
from WFB_Army.models import Army

class StratagemPhase(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return '%s' % self.name

class Stratagem(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    cost = models.CharField(max_length=10)
    type = models.CharField(max_length=64)
    phase_id = models.ForeignKey(StratagemPhase,on_delete=models.SET_NULL,null=True,related_name='stratagem_ids',db_column="phase_id")
    army_id = models.ForeignKey(Army,on_delete=models.SET_NULL,null=True,related_name='stratagem_ids',db_column="army_id")

    def __str__(self):
        return '%s' % self.name
