from django.db import models
from django.conf import settings
from WFB_Army.models import Army
from WFB_Objective.models import Objective
from WFB_Scenario.models import Scenario

# Create your models here.
class Match(models.Model):
    player1_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,related_name='game_p1_ids')
    player2_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,related_name='game_p2_ids')
    army_p1_id = models.ForeignKey(Army, on_delete=models.SET_NULL, null=True,related_name='game_p1_ids')
    army_p2_id = models.ForeignKey(Army, on_delete=models.SET_NULL, null=True,related_name='game_p2_ids')
    scenario_id = models.ForeignKey(Scenario,on_delete=models.SET_NULL, null=True, related_name='game_ids')
    cp_p1 = models.IntegerField(default=0)
    cp_p2 = models.IntegerField(default=0)
    cp_p1_used_before_battle = models.IntegerField(default=0)
    cp_p2_used_before_battle = models.IntegerField(default=0)
    date = models.DateField(blank=True)
    location = models.CharField(max_length=64,blank=True)
    score_no_details = models.BooleanField()
    score_p1 = models.IntegerField(blank=True,null=True)
    score_p2 = models.IntegerField(blank=True,null=True)

    objective1_p1_id = models.ForeignKey(Objective,on_delete=models.SET_NULL, null=True,related_name='game_objective1_p1_ids')
    objective2_p1_id = models.ForeignKey(Objective,on_delete=models.SET_NULL, null=True,related_name='game_objective2_p1_ids')
    objective3_p1_id = models.ForeignKey(Objective,on_delete=models.SET_NULL, null=True,related_name='game_objective3_p1_ids')
    objective1_p2_id = models.ForeignKey(Objective,on_delete=models.SET_NULL, null=True,related_name='game_objective1_p2_ids')
    objective2_p2_id = models.ForeignKey(Objective,on_delete=models.SET_NULL, null=True,related_name='game_objective2_p2_ids')
    objective3_p2_id = models.ForeignKey(Objective,on_delete=models.SET_NULL, null=True,related_name='game_objective3_p2_ids')

    def __str__(self):
        return '%s' % self.id

    class Meta:
        ordering = ['-date']

class MatchLine(models.Model):

    match_id = models.ForeignKey(Match, on_delete=models.CASCADE, null=True,blank=True, related_name='line_ids')
    player = models.IntegerField()
    primary_score = models.IntegerField()
    secondary1_score = models.IntegerField()
    secondary2_score = models.IntegerField()
    secondary3_score = models.IntegerField()
    other_score = models.IntegerField()
    cp_used = models.IntegerField()

    def __str__(self):
        return '%s' % self.id
