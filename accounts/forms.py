from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Recruiter
from django.contrib.auth.forms import AuthenticationForm
from companys.models import Company

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'phone', 'country', 'city', 'photo', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'phone', 'country', 'city', 'photo', 'projects', 'about_me')


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', strip=False, widget=forms.PasswordInput)








class RecruiterRegistrationForm(UserCreationForm):
    company_id = forms.ModelChoiceField(queryset=Company.objects.all(), label='Company')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'company_id']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_recruiter = True  # Устанавливаем флаг, что это рекрутер
        if commit:
            user.save()
            company = self.cleaned_data['company_id']
            Recruiter.objects.create(user=user, company_id=company, username=user.username, password=user.password)
        return user


class RecruiterAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput)