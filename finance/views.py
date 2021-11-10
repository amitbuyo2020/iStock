from django.db.models import query
from django.http.response import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import BalanceSheet, Company, IncomeStatement
from django.views.generic import ListView
# Create your views here.


def home(request):
    return render(request, 'finance/home.html')

def listed_companies(request):
    companies = Company.objects.all()

    context = {
        'dev_banks': companies.filter(category="Development Bank")
    }

    return render(request, 'finance/listed_companies.html', context=context)


def company_detail(request, pk):
    company = get_object_or_404(Company, id=pk)
    context = {
        'company': company
    }

    return render(request, 'finance/company_detail.html', context)

  
class CompanyReports(ListView):
    model = BalanceSheet
    template_name = 'finance/asset_lists.html'
    context_object_name = 'sheets'


    def get_queryset(self):
        company = get_object_or_404(Company, id=self.kwargs.get('pk'))
        return BalanceSheet.objects.filter(company_name=company)


class IncomeReports(ListView):
    model = IncomeStatement
    template_name = 'finance/asset_lists.html'
    context_object_name = 'incomes'


    def get_queryset(self):
        company = get_object_or_404(Company, id=self.kwargs.get('pk'))
        return IncomeStatement.objects.filter(company_name=company)
