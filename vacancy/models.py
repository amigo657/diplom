# vacancy/models.py
from django.db import models
from companys.models import Company
from django.conf import settings

class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.IntegerField()
    work_time = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    recruiter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vacancies')

    def __str__(self):
        return self.title