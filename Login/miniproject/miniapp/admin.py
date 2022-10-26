from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import final_class

@admin.register(final_class)
class final_classAdmin(ImportExportModelAdmin):
        list_display=('roll_no','branch','year','section','mid','sub_code','marks')