from django.urls import path
from .views import privilegy, buy_privilege

urlpatterns = [
    path('', privilegy, name = "privilegy_page"),
    path('buy/<int:privilege_id>/', buy_privilege, name='buy_privilege')
]