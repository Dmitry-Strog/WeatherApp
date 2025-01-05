from django import forms


class CitySearchForm(forms.Form):
    city = forms.CharField(
        label='Город',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите местоположение',
        }),
        required=True,
    )
