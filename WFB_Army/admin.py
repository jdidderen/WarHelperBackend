from django.contrib import admin
from .models import Army
from import_export.admin import ImportExportModelAdmin

@admin.register(Army)
class ArmyAdmin(ImportExportModelAdmin):
    pass