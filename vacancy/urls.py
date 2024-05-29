from django.urls import path
from .views import vacancy_page

urlpatterns = [
    path('', vacancy_page, name = "vacancy_page"),
]
