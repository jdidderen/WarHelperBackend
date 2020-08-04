from django.contrib import admin
from .models import MatchRequest
from import_export.admin import ImportExportModelAdmin

@admin.register(MatchRequest)
class MatchRequestAdmin(ImportExportModelAdmin):
    pass