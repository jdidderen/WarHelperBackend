from django.contrib import admin
from .models import Match,MatchLine
from import_export.admin import ImportExportModelAdmin

@admin.register(Match)
class MatchTypeAdmin(ImportExportModelAdmin):
    pass

@admin.register(MatchLine)
class MatchLineAdmin(ImportExportModelAdmin):
    pass