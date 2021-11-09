from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import UserProfile, CustomUser, Group

class RegistrationForm(forms.Form):
    login = forms.CharField(max_length=20, required=True, label='login')
    password = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput, label='password')
    password_repeat = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput, label='password repeat')

    def clean_login(self):
        data = self.cleaned_data['login']
        if len(data) < 3:
            raise ValidationError(_('Логин должен быть длиной более 2 символов'), code='invalid')
        return data

    def clean_password(self):
        data = self.cleaned_data['password']
        if len(data) < 5:
            raise ValidationError(_('Пароль должен быть длиной более 4 символов'), code='invalid')
        return data

    def clean_password_repeat(self):
        data = self.cleaned_data['password_repeat']
        if data != self.cleaned_data['password']:
            raise ValidationError(_('Пароли не совпадают'), code='invalid')
        return data

class AuthorizationForm(forms.Form):
    login = forms.CharField(max_length=20, required=True, label='login')
    password = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput, label='password')
    remember_me = forms.BooleanField(required=False)


class EditProfile(forms.ModelForm):
    password = forms.CharField(max_length=20, min_length=5, widget=forms.PasswordInput, label='Change password',
                               required=False)

    photo = forms.ImageField(label=_('Photo'), widget=forms.FileInput)
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'password', 'photo']

    def __init__(self, *args, **kwargs):
        super(EditProfile, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['photo'].widget.attrs['class'] = 'form-control-file'

class EditGroup(forms.ModelForm):
    group = forms.ModelChoiceField(queryset=Group.objects, empty_label=None)
    class Meta:
        model = CustomUser
        fields = ['group']

    def __init__(self, *args, **kwargs):
        super(EditGroup, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'