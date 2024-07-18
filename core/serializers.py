from rest_framework import serializers

from core.models import ImpressionStatistics


class ImpressionStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImpressionStatistics
        fields = (
            "city_name",
            "impressions",
        )
