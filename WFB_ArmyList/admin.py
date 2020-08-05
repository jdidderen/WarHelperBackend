from django.contrib import admin
from .models import ArmyList
from import_export.admin import ImportExportModelAdmin


@admin.register(ArmyList)
class ArmyListAdmin(ImportExportModelAdmin):
    pass