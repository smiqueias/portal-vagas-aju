from django.contrib import admin
from .models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('title','company_name','description','contact','location','occupation','contract', 'salary')
    list_display_links = ('title','contact')
    search_fields = ('title',)
admin.site.register(Job,JobAdmin)    