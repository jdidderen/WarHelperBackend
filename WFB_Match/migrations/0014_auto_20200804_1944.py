# Generated by Django 3.0.8 on 2020-08-04 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WFB_Objective', '0004_auto_20200801_1456'),
        ('WFB_Army', '0001_initial'),
        ('WFB_Scenario', '0004_auto_20200731_0038'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WFB_Match', '0013_auto_20200731_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='army_p1_id',
            field=models.ForeignKey(db_column='army_p1_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_p1_ids', to='WFB_Army.Army'),
        ),
        migrations.AlterField(
            model_name='match',
            name='army_p2_id',
            field=models.ForeignKey(db_column='army_p2_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_p2_ids', to='WFB_Army.Army'),
        ),
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='location',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='objective1_p1_id',
            field=models.ForeignKey(db_column='objective1_p1_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_objective1_p1_ids', to='WFB_Objective.Objective'),
        ),
        migrations.AlterField(
            model_name='match',
            name='objective1_p2_id',
            field=models.ForeignKey(db_column='objective1_p2_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_objective1_p2_ids', to='WFB_Objective.Objective'),
        ),
        migrations.AlterField(
            model_name='match',
            name='objective2_p1_id',
            field=models.ForeignKey(db_column='objective2_p1_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_objective2_p1_ids', to='WFB_Objective.Objective'),
        ),
        migrations.AlterField(
            model_name='match',
            name='objective2_p2_id',
            field=models.ForeignKey(db_column='objective2_p2_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_objective2_p2_ids', to='WFB_Objective.Objective'),
        ),
        migrations.AlterField(
            model_name='match',
            name='objective3_p1_id',
            field=models.ForeignKey(db_column='objective3_p1_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_objective3_p1_ids', to='WFB_Objective.Objective'),
        ),
        migrations.AlterField(
            model_name='match',
            name='objective3_p2_id',
            field=models.ForeignKey(db_column='objective3_p2_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_objective3_p2_ids', to='WFB_Objective.Objective'),
        ),
        migrations.AlterField(
            model_name='match',
            name='player1_id',
            field=models.ForeignKey(db_column='player1_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_p1_ids', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='match',
            name='player2_id',
            field=models.ForeignKey(db_column='player2_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_p2_ids', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='match',
            name='scenario_id',
            field=models.ForeignKey(db_column='scenario_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_ids', to='WFB_Scenario.Scenario'),
        ),
        migrations.AlterField(
            model_name='matchline',
            name='match_id',
            field=models.ForeignKey(blank=True, db_column='match_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='line_ids', to='WFB_Match.Match'),
        ),
    ]