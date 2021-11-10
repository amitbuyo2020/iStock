from django.urls import path
from . import views
from .views import CompanyReports, IncomeReports

urlpatterns = [
    path('', views.home, name='home'),
    path('listed_companies/', views.listed_companies, name='Listed_Companies'),
    path('listed_companies/<int:pk>', views.company_detail, name='detail'),
    path('reports/<int:pk>', CompanyReports.as_view(), name='reports'),
    path('reports/<int:pk>', IncomeReports.as_view())

]