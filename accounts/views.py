from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from companys.models import Company
from .forms import CustomUserCreationForm, CustomAuthenticationForm, RecruiterRegistrationForm, RecruiterAuthenticationForm, ProfileForm

def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            authenticated_user = authenticate(request, username=user.username, password=form.cleaned_data['password1'])
            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})


def profile(request):
    user = request.user
    user.daily_bonus()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile_page')  # Обновите этот URL на URL страницы профиля
    else:
        form = ProfileForm(instance=user)

    privilege_expiry = None
    if user.privilege and user.status_time:
        privilege_expiry = user.status_time + user.privilege.time  # Расчет срока действия привилегии

    return render(request, 'profile.html', {
        'form': form,
        'privilege_expiry': privilege_expiry,
    })


def log_out(request):
    logout(request)
    return redirect('home')

# для рекрутера
def recruiter_register(request):
    if request.method == 'POST':
        form = RecruiterRegistrationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            # После успешной регистрации авторизуем пользователя и перенаправляем
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = RecruiterRegistrationForm()
    companies = Company.objects.all()
    return render(request, 'recruiter_register.html', {'form': form, 'companies': companies})

def recruiter_login(request):
    if request.method == 'POST':
        form = RecruiterAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_recruiter:
                login(request, user)
                return redirect('home')
            else:
                # Если пользователь не найден или не является рекрутером, отобразить сообщение об ошибке
                return render(request, 'recruiter_login.html', {'form': form, 'error_message': 'Invalid username or password'})
    else:
        form = RecruiterAuthenticationForm()
    return render(request, 'recruiter_login.html', {'form': form})