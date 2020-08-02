from django.db import models
from django.conf import settings

class ScenarioType(models.Model):
    name = models.CharField(max_length=64)
    point_limit = models.CharField(max_length=64)

    def __str__(self):
        return '%s' % self.name

# Create your models here.
class Scenario(models.Model):
    name = models.CharField(max_length=64)
    type_id = models.ForeignKey(ScenarioType,on_delete=models.SET_NULL,null=True,related_name='scenario_ids')
    rules = models.ImageField(blank=True, null=True)
    deployment = models.ImageField(null=True,default=True)

    def __str__(self):
        return '%s' % self.name

    def get_rules_url(self):
        if self.rules:
            return self.rules.url
        else:
            return ''

    def get_deployment_url(self):
        if self.deployment:
            return self.deployment.url
        else:
            return ''