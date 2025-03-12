# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from batch1.models import CsvData

class CsvDataAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2', 'field3')
    actions = ['bulk_delete']

    def bulk_delete(self, request, queryset):
        queryset.delete()
    bulk_delete.short_description = "Delete selected records"

admin.site.register(CsvData, CsvDataAdmin)
