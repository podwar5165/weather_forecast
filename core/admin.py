from django.contrib import admin

from core.models import ImpressionStatistics


@admin.register(ImpressionStatistics)
class ImpressionStatisticsAdmin(admin.ModelAdmin):
    list_display = ("city_name", "impressions")
