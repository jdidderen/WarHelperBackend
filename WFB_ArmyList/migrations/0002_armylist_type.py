# Generated by Django 3.0.8 on 2020-08-05 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WFB_ArmyList', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='armylist',
            name='type',
            field=models.CharField(blank=True, choices=[('aln', 'ALN'), ('bsc', 'BattleScribe')], max_length=10, null=True),
        ),
    ]