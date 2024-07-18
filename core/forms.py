from django import forms


class CheckWeatherForm(forms.Form):
    city_name = forms.CharField()

    def __init__(self, *args, **kwargs):
        city_name = kwargs.pop("city_name", "")
        super().__init__(*args, **kwargs)
        self.fields["city_name"].initial = city_name
        self.fields["city_name"].widget.attrs["placeholder"] = "Введите название города"
        self.fields["city_name"].widget.attrs["class"] = "form-control"
