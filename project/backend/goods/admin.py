from django.contrib import admin
from goods.models import Good


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ["title", "min_price", "price_coefficient", "available"]
    list_editable = ["min_price", "price_coefficient", "available"]
    list_filter = ["available"]
