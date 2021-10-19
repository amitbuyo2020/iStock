from django.shortcuts import render
from .models import Company
# Create your views here.


def home(request):
    return render(request, 'finance/home.html')

def listed_companies(request):
    companies = Company.objects.all()

    context = {
        'companies': companies
    }

    return render(request, 'finance/listed_companies.html', context=context)