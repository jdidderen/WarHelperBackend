from django.db import models
from django.conf import settings

class MatchRequest(models.Model):
    date = models.DateField()
    player_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,related_name='request_ids',db_column="player_id")

    def __str__(self):
        return '%s' % self.player_id.username
