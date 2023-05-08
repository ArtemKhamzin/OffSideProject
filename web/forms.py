from datetime import datetime
from django import forms
from django.contrib.auth import get_user_model
from web.models import Blog, BlogTag

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            self.add_error("password", "Пароли не совпадают")
        return cleaned_data

    class Meta:
        model = User
        fields = ("email", "username", "password", "password2")


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class BlogForm(forms.ModelForm):
    publication_date = forms.CharField(widget=forms.HiddenInput, initial=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def save(self, commit=True):
        self.instance.user = self.initial['user']
        return super().save(commit)

    class Meta:
        model = Blog
        fields = ('title', 'short_description', 'description', 'publication_date', 'image', 'tags')
        widgets = {
            'short_description': forms.Textarea,
            'description': forms.Textarea
        }


class BlogTagForm(forms.ModelForm):
    class Meta:
        model = BlogTag
        fields = ('title',)


class BlogFilterForm(forms.Form):
    search = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Поиск"}), required=False)
