# Generated by Django 3.0.8 on 2020-08-02 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WFB_Stratagem', '0003_auto_20200728_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stratagem',
            name='cost',
            field=models.CharField(max_length=10),
        ),
    ]
