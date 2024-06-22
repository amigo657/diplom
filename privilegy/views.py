from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Privilege
from .forms import PaymentForm
from django.utils import timezone
from vacancy.models import Vacancy
import random

def privilegy(request):
    privileges = Privilege.objects.all()
    for privilege in privileges:
        privilege.description_list = privilege.description.split(";")
    return render(request, "privilegy_page.html", {'privileges': privileges})

@login_required
def buy_privilege(request, privilege_id):
    privilege = get_object_or_404(Privilege, id=privilege_id)
    user = request.user

    if user.internal_currency >= privilege.cost:
        user.internal_currency -= privilege.cost
        user.privilege = privilege
        user.status_time = timezone.now()
        user.save()
        return redirect('home')
    else:
        return render(request, 'privilegy/buy_privilege.html', {'privilege': privilege, 'error': 'Not enough internal currency'})

def random_vacancy_detail(request):
    vacancy_ids = Vacancy.objects.values_list('id', flat=True)
    if vacancy_ids:
        random_id = random.choice(vacancy_ids)
        random_vacancy = get_object_or_404(Vacancy, id=random_id)
        return redirect('vacancy_detail', vacancy_id=random_vacancy.id)
    else:
        return redirect('vacancy_list')