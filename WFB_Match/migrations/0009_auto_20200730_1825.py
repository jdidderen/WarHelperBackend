# Generated by Django 3.0.8 on 2020-07-30 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WFB_Objective', '0001_initial'),
        ('WFB_Scenario', '0001_initial'),
        ('WFB_Match', '0008_remove_match_point_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='objective1_p1_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_objective1_p1_ids', to='WFB_Objective.Objective'),
        ),
        migrations.AddField(
            model_name='match',
            name='objective1_p2_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_objective1_p2_ids', to='WFB_Objective.Objective'),
        ),
        migrations.AddField(
            model_name='match',
            name='objective2_p1_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_objective2_p1_ids', to='WFB_Objective.Objective'),
        ),
        migrations.AddField(
            model_name='match',
            name='objective2_p2_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_objective2_p2_ids', to='WFB_Objective.Objective'),
        ),
        migrations.AddField(
            model_name='match',
            name='objective3_p1_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_objective3_p1_ids', to='WFB_Objective.Objective'),
        ),
        migrations.AddField(
            model_name='match',
            name='objective3_p2_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_objective3_p2_ids', to='WFB_Objective.Objective'),
        ),
        migrations.AddField(
            model_name='match',
            name='scenario_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_ids', to='WFB_Scenario.Scenario'),
        ),
    ]
