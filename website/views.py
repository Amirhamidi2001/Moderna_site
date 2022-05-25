from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    return render(request, 'website/contact.html')


def portfolio_view(request):
    return render(request, 'website/portfolio.html')


def services_view(request):
    return render(request, 'website/services.html')


def team_view(request):
    return render(request, 'website/team.html')
