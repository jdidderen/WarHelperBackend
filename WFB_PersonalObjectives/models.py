from django.db import models
from django.conf import settings

class PersonalObjective(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    date = models.DateField()
    player_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='personal_objective_ids',db_column="player_id")

    def __str__(self):
        return '%s' % self.name
