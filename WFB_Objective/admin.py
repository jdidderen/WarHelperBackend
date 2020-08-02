from django.contrib import admin
from .models import Objective,ObjectiveType
from import_export.admin import ImportExportModelAdmin

@admin.register(Objective)
class ObjectiveAdmin(ImportExportModelAdmin):
    pass

@admin.register(ObjectiveType)
class ObjectiveTypeAdmin(ImportExportModelAdmin):
    pass