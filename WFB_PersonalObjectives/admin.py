from django.contrib import admin
from .models import PersonalObjective
from import_export.admin import ImportExportModelAdmin


@admin.register(PersonalObjective)
class PersonalObjectiveAdmin(ImportExportModelAdmin):
    pass