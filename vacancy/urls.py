from django.urls import path
from .views import vacancy_list, vacancy_detail, vacancy_create, vacancy_delete, company_detail, apply_for_vacancy, recruiter_responses, UserProfileDetailView

urlpatterns = [
    path('', vacancy_list, name = "vacancy_list"),
    path('<int:vacancy_id>/', vacancy_detail, name='vacancy_detail'),
    path('create/', vacancy_create, name='vacancy_create'),
    path('<int:vacancy_id>/delete/', vacancy_delete, name='vacancy_delete'),
    path('company/<int:company_id>/', company_detail, name='company_detail'),
    path('apply/<int:vacancy_id>/', apply_for_vacancy, name='apply_for_vacancy'),
    path('recruiter/responses/', recruiter_responses, name='recruiter_responses'),
    path('user/<int:pk>/', UserProfileDetailView.as_view(), name='user_profile_detail'),
]