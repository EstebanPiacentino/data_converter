from django.contrib import admin
from backend.models import *

# Export as CSV
import csv
from django.http import HttpResponse

from django.contrib.admin import SimpleListFilter


class EventLogAdmin(admin.ModelAdmin):

    readonly_fields = ('id',)
    fields = ('id', 'timestamp', 'spss_file', 'excel_file')
    list_display = ('id', 'timestamp', 'spss_file', 'excel_file')


admin.site.register(EventLog, EventLogAdmin)