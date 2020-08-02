from django.contrib import admin
from .models import Stratagem
from .models import StratagemPhase
from import_export.admin import ImportExportModelAdmin

@admin.register(Stratagem)
class StratagemAdmin(ImportExportModelAdmin):
    pass

@admin.register(StratagemPhase)
class StratagemPhaseAdmin(ImportExportModelAdmin):
    pass