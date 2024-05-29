from django.contrib.auth.models import AbstractUser
from django.db import models
from companys.models import Company  # Убедитесь, что импортировали модель Company

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    projects = models.TextField(blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    status_time = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    is_recruiter = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.username

class Recruiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='recruiter_profile')
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)  # Убедитесь, что это связано с Company
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
