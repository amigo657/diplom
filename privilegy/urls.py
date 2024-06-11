from django.urls import path
from .views import privilegy, buy_privilege, random_vacancy_detail

urlpatterns = [
    path('', privilegy, name = "privilegy_page"),
    path('buy/<int:privilege_id>/', buy_privilege, name='buy_privilege'),
    path('random_vacancy/', random_vacancy_detail, name='random_vacancy'),
]