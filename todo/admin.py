from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'completed')
    list_filter = ('created_date', 'completed')
    search_fields = ('title',)
    ordering = ('-created_date',)

admin.site.register(Task, TaskAdmin)
