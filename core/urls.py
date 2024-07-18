from django.urls import include, path
from rest_framework import routers

from .views import GetCityNamesView, ImpressionStatisticsViewSet, IndexView

router = routers.SimpleRouter()
router.register("impression-statistics", ImpressionStatisticsViewSet)

patterns = (
    [
        path("", IndexView.as_view(), name="index"),
        path("city-names/", GetCityNamesView.as_view(), name="city-names"),
    ],
    "core",
)

urlpatterns = [path("", include(patterns))]
urlpatterns += router.urls
