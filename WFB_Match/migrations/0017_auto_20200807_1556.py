# Generated by Django 3.0.8 on 2020-08-07 13:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('WFB_Match', '0016_auto_20200807_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
