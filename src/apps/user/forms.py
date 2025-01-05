from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.hashers import make_password

from apps.user.models import CustomUser


class LoginForm(forms.Form):
    login = forms.CharField(label="Логин", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите логин',
    }))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите пароль',
    }))


class RegisterForm(forms.ModelForm):
    login = forms.CharField(label="Логин", widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }), label="Пароль")
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }), label="Подтвердите пароль")

    class Meta:
        model = CustomUser
        fields = ['login']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
