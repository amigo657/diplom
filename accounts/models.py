from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models
from companys.models import Company  # Убедитесь, что импортировали модель Company
from privilegy.models import Privilege

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    projects = models.TextField(blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    privilege = models.OneToOneField(Privilege, on_delete=models.SET_NULL, blank=True, null=True)
    status_time = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    internal_currency = models.PositiveIntegerField(default=0)
    num_applications = models.PositiveIntegerField(default=0)
    is_recruiter = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.username
    
    def add_currency(self, amount):
        self.internal_currency += amount
        self.save()

    def apply_for_vacancy(self, vacancy):
        self.add_currency(10)  # Example amount for applying for a vacancy

    def apply_for_multiple_vacancies(self, num_vacancies):
        if num_vacancies >= 5:
            self.add_currency(50)  # Example amount for applying for 5 vacancies
        if num_vacancies >= 10:
            self.add_currency(100)  # Example amount for applying for 10 vacancies

    def daily_bonus(self):
        if not self.status_time or timezone.now() - self.status_time > timezone.timedelta(days=1):
            self.add_currency(20)
            self.status_time = timezone.now()
            self.save()

class Recruiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='recruiter_profile')
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)  # Убедитесь, что это связано с Company
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    
    def get_company(self):
        return self.company_id
