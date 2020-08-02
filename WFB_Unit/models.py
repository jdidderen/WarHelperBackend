from django.db import models
from WFB_Army.models import Army

class UnitType(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return '%s' % self.name

class Unit(models.Model):
    name = models.CharField(max_length=64)
    unit_type_id = models.ForeignKey(UnitType,on_delete=models.SET_NULL,null=True,related_name='unit_ids')
    army_id = models.ForeignKey(Army,on_delete=models.SET_NULL,null=True,related_name='unit_ids')

    def __str__(self):
        return '%s' % self.name
