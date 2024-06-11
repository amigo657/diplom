# vacancy/forms.py
from django import forms
from .models import Vacancy, Response

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'description', 'salary', 'work_time', 'city']


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['vacancy']  # Поле vacancy будет скрытым
        widgets = {'vacancy': forms.HiddenInput()}