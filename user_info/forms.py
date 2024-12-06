from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import BankUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = BankUser
        fields = UserCreationForm.Meta.fields + ('age', )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = BankUser
        fields = UserChangeForm.Meta.fields
