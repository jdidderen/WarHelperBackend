from django.contrib import admin
from .models import ScenarioType,Scenario
from import_export.admin import ImportExportModelAdmin

@admin.register(Scenario)
class ScenarioAdmin(ImportExportModelAdmin):
    pass

@admin.register(ScenarioType)
class ScenarioTypeAdmin(ImportExportModelAdmin):
    pass