from django.test import TestCase
from django.urls import reverse_lazy

from core.models import ImpressionStatistics


class IndexPageTest(TestCase):

    def test_index_page(self):
        response = self.client.get(reverse_lazy("core:index"))
        self.assertEqual(response.status_code, 200)

    def test_get_weather(self):
        city_name = "San Francisco"
        data = {
            "city_name": city_name,
        }
        self.client.post(reverse_lazy("core:index"), data=data)
        self.assertEqual(
            ImpressionStatistics.objects.filter(city_name=city_name).count(), 1
        )
