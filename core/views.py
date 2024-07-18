from django.db.models import F
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets

from core.forms import CheckWeatherForm
from core.models import ImpressionStatistics
from core.serializers import ImpressionStatisticsSerializer
from core.utils import get_city_data, get_city_names, get_weather_by_geo_data


class IndexView(FormView):
    form_class = CheckWeatherForm
    template_name = "index.html"
    success_url = reverse_lazy("core:index")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"city_name": self.request.COOKIES.get("city_name")})
        return kwargs

    def form_valid(self, form):
        response = super().form_valid(form)
        response.set_cookie("city_name", form.cleaned_data.get("city_name"))
        data = get_city_data(form.cleaned_data.get("city_name"))

        if data.get("status"):
            latitude: float = data.get("result").get("latitude", 0)
            longitude: float = data.get("result").get("longitude", 0)
            weather = get_weather_by_geo_data(latitude, longitude)
            response.set_cookie("temperature", weather.get("result").get("temperature"))
            response.set_cookie("wind_speed", weather.get("result").get("wind_speed"))
            statistic = ImpressionStatistics.objects.filter(
                city_name=form.cleaned_data.get("city_name")
            ).first()
            if not statistic:
                ImpressionStatistics.objects.create(
                    city_name=form.cleaned_data.get("city_name"), impressions=1
                )
            else:
                statistic.impressions = F("impressions") + 1
                statistic.save(update_fields=["impressions"])
        return response


class GetCityNamesView(TemplateView):
    template_name = "city_names.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["names"] = get_city_names(self.request.GET.get("name"))
        return context


class ImpressionStatisticsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = ()
    queryset = ImpressionStatistics.objects
    serializer_class = ImpressionStatisticsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("city_name",)
