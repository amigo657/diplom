from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Privilege
from .forms import PaymentForm
from django.utils import timezone
from vacancy.models import Vacancy
import random

def privilegy(request):
    privilegys = Privilege.objects.all()
    return render(request, "privilegy_page.html", {'privilegys': privilegys})

@login_required
def buy_privilege(request, privilege_id):
    privilege = Privilege.objects.get(id=privilege_id)
    
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Назначение привилегии пользователю
            user = request.user
            user.privilege = privilege
            user.status_time = timezone.now()
            user.save()
            return redirect('home')
    else:
        form = PaymentForm()

    return render(request, 'privilegy/buy_privilege.html', {'form': form, 'privilege': privilege})

def random_vacancy_detail(request):
    vacancy_ids = Vacancy.objects.values_list('id', flat=True)
    if vacancy_ids:
        random_id = random.choice(vacancy_ids)
        random_vacancy = get_object_or_404(Vacancy, id=random_id)
        return redirect('vacancy_detail', vacancy_id=random_vacancy.id)
    else:
        return redirect('vacancy_list')