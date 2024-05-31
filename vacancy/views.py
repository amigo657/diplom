# vacancy/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from .models import Vacancy
from companys.models import Company
from .forms import VacancyForm

# Вывод списка вакансий
def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancy_list.html', {'vacancies': vacancies})

# Просмотр вакансии
def vacancy_detail(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    return render(request, 'vacancy_detail.html', {'vacancy': vacancy})

# Просмотр компании и её вакансий
def company_detail(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    vacancies = Vacancy.objects.filter(company=company)
    return render(request, 'company_detail.html', {'company': company, 'vacancies': vacancies})

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
