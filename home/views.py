from django.shortcuts import render

def home_page(request):
    return render(request, "home.html", {})

def contacts(request):
    return render(request, "contacts_page.html", {})