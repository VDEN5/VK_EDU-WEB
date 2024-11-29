from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Quests, Answer


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm = forms.BooleanField(widget=forms.CheckboxInput)

    def clean_username(self):
        return self.cleaned_data['username'].lower().strip()

class QuestForm(forms.ModelForm):
    #tags=forms.JSONField(default=list)
    tags = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Теги, разделенные запятыми'}), required=False)
    class Meta:
        model = Quests
        fields = ['quest_data', 'tags']

class AnsForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['data']

class UserForm(forms.ModelForm):
    # Замена
    password = forms.CharField(widget=forms.PasswordInput)

    # Новое поле
    password_confirmation = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean(self):
        data = super().clean()

        if data['password'] != data['password_confirmation']:
            raise ValidationError('Passwords do not match')

        return data

    def save(self, commit=True):
        user = super().save(commit=False)

        user.set_password(self.cleaned_data['password'])

        user.save()

        return user