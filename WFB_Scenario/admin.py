from django.contrib import admin
from .models import ScenarioType,Scenario
# Register your models here.
admin.site.register(Scenario)
admin.site.register(ScenarioType)
