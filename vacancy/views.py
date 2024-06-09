# vacancy/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from .models import Vacancy, Response
from companys.models import Company
from .forms import VacancyForm, ResponseForm
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.views.generic import DetailView


# Функция для фильтрации вакансий
def vacancy_list(request):
    category = request.GET.get('category')
    location = request.GET.get('location')
    keyword = request.GET.get('keyword')
    min_salary = request.GET.get('min_salary')
    max_salary = request.GET.get('max_salary')

    vacancies = Vacancy.objects.all()

    if category:
        vacancies = vacancies.filter(category=category)
    
    if location:
        vacancies = vacancies.filter(city=location)
    
    if keyword:
        vacancies = vacancies.filter(
            Q(title__icontains=keyword) |
            Q(company__name__icontains=keyword)
        )
    
    if min_salary:
        vacancies = vacancies.filter(salary__gte=min_salary)
    
    if max_salary:
        vacancies = vacancies.filter(salary__lte=max_salary)
    
    context = {
        'vacancies': vacancies,
    }
    
    return render(request, 'vacancy_list.html', context)

# Просмотр вакансии
def vacancy_detail(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    user_response = None
    if request.user.is_authenticated:
        user_response = Response.objects.filter(user=request.user, vacancy=vacancy).first()
    context = {
        'vacancy': vacancy,
        'user_response': user_response,
    }
    return render(request, 'vacancy_detail.html', context)

# Просмотр компании и её вакансий
def company_detail(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    vacancies = Vacancy.objects.filter(company=company)
    return render(request, 'company_detail.html', {'company': company, 'vacancies': vacancies})

# Обработка откликов
@login_required
def apply_for_vacancy(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.user = request.user
            response.save()
            return redirect('vacancy_detail', vacancy_id=vacancy.id)
    else:
        form = ResponseForm(initial={'vacancy': vacancy})

    return render(request, 'apply_for_vacancy.html', {'form': form, 'vacancy': vacancy})

# Создание вакансии
@login_required
def vacancy_create(request):
    if not hasattr(request.user, 'recruiter_profile'):
        raise PermissionDenied("You do not have permission to create a vacancy.")

    recruter_profile = request.user.recruiter_profile        

    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.recruiter = request.user
            vacancy.company = recruter_profile.get_company()
            vacancy.save()
            return redirect('vacancy_list')
    else:
        form = VacancyForm()
    return render(request, 'vacancy_form.html', {'form': form})

# Удаление вакансии
@login_required
def vacancy_delete(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    if request.user != vacancy.recruiter:
        return HttpResponseForbidden()
    if request.method == 'POST':
        vacancy.delete()
        return redirect('vacancy_list')
    print('work0')
    return render(request, 'vacancy_confirm_delete.html', {'vacancy': vacancy})

# Отображение откликов
@login_required
def recruiter_responses(request):
    if not request.user.is_recruiter:
        return redirect('vacancy_list')
    
    if request.user.is_superuser:
        responses = Response.objects.all()
    else:
        responses = Response.objects.filter(vacancy__recruiter=request.user)
    return render(request, 'recruiter_responses.html', {'responses': responses})


User = get_user_model()

class UserProfileDetailView(DetailView):
    model = User
    template_name = 'user_profile_detail.html'
    context_object_name = 'user_profile'