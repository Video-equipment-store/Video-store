from django.contrib import admin
from services.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["title", "min_price"]
    list_editable = ["min_price"]
    # list_filter = ["available"]
