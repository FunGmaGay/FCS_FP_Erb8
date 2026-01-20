from django.contrib import admin
from .models import Tutor

class TutorAdmin(admin.ModelAdmin):
    list_display = 'tutor_name', 'tagline1', 'experience', 'is_published'
    list_filter = ('tutor_name', 'is_published')
    list_display_links = ('tutor_name', 'is_published')
    search_fields = ('tutor_name', 'is_published')
    list_per_page = 25

admin.site.register(Tutor, TutorAdmin)
# Register your models here.
