from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    vacancy_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
