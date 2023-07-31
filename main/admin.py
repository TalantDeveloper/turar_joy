from django.contrib import admin
from .models import Faculties, Application
from modeltranslation.admin import TranslationAdmin


@admin.register(Faculties)
class FacultiesAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'link_name')
    list_display_link = ('id', 'name', 'link_name')
    search_fields = ('name', 'link_name')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number', 'faculty', 'course', 'i_va_ii', 'temir_daftar', 'yetim')
    list_display_links = ('id', 'full_name', 'phone_number')
    search_fields = ('full_name', 'faculty', 'course')
    filter = ('faculty', 'course')


