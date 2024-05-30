from django.db import models

class Privilege(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DurationField()

    def __str__(self):
        return self.title