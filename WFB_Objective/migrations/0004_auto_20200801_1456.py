# Generated by Django 3.0.8 on 2020-08-01 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WFB_Objective', '0003_auto_20200730_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objective',
            name='description',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
