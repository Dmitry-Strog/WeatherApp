from django import forms


class CitySearchForm(forms.Form):
    city = forms.CharField(label="Найти город", required=False)
