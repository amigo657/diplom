from django.urls import path
from .views import privilegy

urlpatterns = [
    path('', privilegy, name = "privilegy_page"),
]
