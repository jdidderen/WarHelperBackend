from django.contrib import admin
from .models import Unit,UnitType
from import_export.admin import ImportExportModelAdmin

@admin.register(Unit)
class UnitAdmin(ImportExportModelAdmin):
    pass

@admin.register(UnitType)
class UnitTypeAdmin(ImportExportModelAdmin):
    pass