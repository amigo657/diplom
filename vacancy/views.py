from django.shortcuts import render

def vacancy_page(request):
    return render(request, "vacancy_page.html", {})