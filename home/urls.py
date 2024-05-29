from django.urls import path
from .views import home_page, contacts

urlpatterns = [
    path('', home_page, name = 'home'),
    path('contacts/', contacts, name = 'contacts_page'),
]
