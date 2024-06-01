from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Privilege
from accounts.models import User
from .forms import PaymentForm
from django.utils import timezone

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