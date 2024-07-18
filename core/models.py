from django.db import models


class ImpressionStatistics(models.Model):
    city_name = models.CharField(max_length=255, unique=True)
    impressions = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name = "Статистика показов"
        verbose_name_plural = "Статистики показов"
