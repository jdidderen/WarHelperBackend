from django.db import models
from django.conf import settings
from WFB_Army.models import Army

LIST_TYPES = (
    ('aln', 'ALN'),
    ('bsc', 'BattleScribe'),
)

class ArmyList(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    army_id = models.ForeignKey(Army, on_delete=models.SET_NULL, null=True,related_name='army_list_ids',db_column="army_id")
    player_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='army_list_ids',db_column="player_id")
    type = models.CharField(max_length=10,blank=True,null=True, choices=LIST_TYPES)

    def __str__(self):
        return '%s' % self.name
