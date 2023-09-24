from django.contrib import admin

from .models import Facility


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "type", "is_active")
    list_filter = ("type", "is_active")
    search_fields = ("name", "address")
    ordering = ("name",)
