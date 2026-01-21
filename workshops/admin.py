from django.contrib import admin
from .models import Workshop

class WorkshopAdmin(admin.ModelAdmin):
    list_display = 'workshop', 'tutor_name', 'start_date', 'is_published'
    list_filter = ('workshop', 'tutor_name')
    list_display_links = ('workshop', 'tutor_name')
    search_fields = ('workshop', 'tutor_name')
    list_per_page = 25

admin.site.register(Workshop, WorkshopAdmin)