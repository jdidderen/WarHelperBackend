# Generated by Django 3.0.8 on 2020-07-29 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WFB_Match', '0002_auto_20200729_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='score_p1',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='score_p2',
            field=models.IntegerField(null=True),
        ),
    ]
