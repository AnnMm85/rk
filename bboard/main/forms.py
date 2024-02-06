from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustUser


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustUser
        fields = ['username', 'avatar', 'email', 'password1', 'password2']


class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=1000, required=False, label='Поиск')


