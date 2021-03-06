# Generated by Django 3.0.8 on 2020-08-10 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WFB_Scenario', '0005_auto_20200804_1949'),
        ('WFB_Army', '0001_initial'),
        ('WFB_Match', '0017_auto_20200807_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='army_p1_id',
            field=models.ForeignKey(blank=True, db_column='army_p1_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_p1_ids', to='WFB_Army.Army'),
        ),
        migrations.AlterField(
            model_name='match',
            name='army_p2_id',
            field=models.ForeignKey(blank=True, db_column='army_p2_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_p2_ids', to='WFB_Army.Army'),
        ),
        migrations.AlterField(
            model_name='match',
            name='player1_id',
            field=models.ForeignKey(blank=True, db_column='player1_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_p1_ids', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='match',
            name='scenario_id',
            field=models.ForeignKey(blank=True, db_column='scenario_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_ids', to='WFB_Scenario.Scenario'),
        ),
        migrations.AlterField(
            model_name='matchline',
            name='cp_used',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='matchline',
            name='other_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='matchline',
            name='player',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='matchline',
            name='primary_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='matchline',
            name='secondary1_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='matchline',
            name='secondary2_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='matchline',
            name='secondary3_score',
            field=models.IntegerField(default=0),
        ),
    ]
