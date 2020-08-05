# Generated by Django 3.0.8 on 2020-08-05 20:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WFB_Army', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArmyList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('shortDescription', models.TextField()),
                ('description', models.TextField()),
                ('army_id', models.ForeignKey(db_column='army_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='army_list_ids', to='WFB_Army.Army')),
                ('player_id', models.ForeignKey(db_column='player_id', on_delete=django.db.models.deletion.CASCADE, related_name='army_list_ids', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
