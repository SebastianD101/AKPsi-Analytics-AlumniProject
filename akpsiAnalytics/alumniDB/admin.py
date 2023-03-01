from django.contrib import admin
from .models import *


class AlumniAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'graduation_date', 'current_company', 'position', 'sphere')
    list_filter = ('sphere', 'position', 'current_company', 'position', 'sphere')
    search_fields = ('name', 'email', 'current_company')

admin.site.register(Alumni, AlumniAdmin)
