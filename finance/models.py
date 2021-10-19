from django.db import models



class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name='category')

    def __str__(self):
        return self.category


class Company(models.Model):
    name = models.CharField(max_length=200, verbose_name='Company Name', unique=True)
    established_date = models.DateField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Asset(models.Model):
    company_name =              models.ForeignKey(Company, on_delete=models.CASCADE)
    year =                      models.CharField(max_length=25, verbose_name='Fiscal Year')
    cash_equiv =                models.CharField(max_length=50, null=True, blank=True, verbose_name='Cash and Cash Equivalent')
    money_at_call =             models.CharField(max_length=50, null=True, blank=True, verbose_name='Money at Call & short notice')
    due_from_nrb =              models.CharField(max_length=50, null=True, blank=True, verbose_name='Due From NRB')
    placement_with_bfis =       models.CharField(max_length=50, null=True, blank=True, verbose_name='Placement with B/FIs')
    loans_advances =            models.CharField(max_length=50, null=True, blank=True, verbose_name='Loans & Advances')
    loans_advances_with_bfis =  models.CharField(max_length=50, null=True, blank=True, verbose_name='Loans & Adavances to B/FIs')
    loans_to_customers =        models.CharField(max_length=50, null=True, blank=True, verbose_name='Loans & Advances to Customers')
    investments =               models.CharField(max_length=50, null=True, blank=True, verbose_name='Investments')
    invest_security =           models.CharField(max_length=50, null=True, blank=True, verbose_name='Investment Security')
    invest_in_subsidiaries =    models.CharField(max_length=50, null=True, blank=True, verbose_name='Investment in Subsidiaries')
    invest_in_associtaes =      models.CharField(max_length=50, null=True, blank=True, verbose_name='Investment in Associates')
    property_investment =       models.CharField(max_length=50, null=True, blank=True, verbose_name='Investment Property')
    other_assets =              models.CharField(max_length=50, null=True, blank=True, verbose_name='Other Assets')
    derive_fin_instruments =    models.CharField(max_length=50, null=True, blank=True, verbose_name='Derivative Financial Instruments')
    trading_assets =            models.CharField(max_length=50, null=True, blank=True, verbose_name='Other Trading Assets')
    current_tax_assets =        models.CharField(max_length=50, null=True, blank=True, verbose_name='Current Tax Assets')
    deferred_tax_assets =       models.CharField(max_length=50, null=True, blank=True, verbose_name='Deferred Tax Assets')
    goodwill_assets =           models.CharField(max_length=50, null=True, blank=True, verbose_name='Goodwill and Intangible Assets')
    property_equipment =        models.CharField(max_length=50, null=True, blank=True, verbose_name='Property & Equipment')
    total_assets =              models.CharField(max_length=50, null=True, blank=True, verbose_name='Total Assets')
    # cash_equiv = models.CharField(max_length=50, null=True, blank=True, verbose_name)

    def __str__(self):
        return self.company_name
    


class IncomeStatement(models.Model):
    company_name =                            models.ForeignKey(Company, on_delete=models.CASCADE)
    year =                                    models.CharField(max_length=20, verbose_name='Fiscal Year')

    int_income =                              models.CharField(max_length=25, null=True, blank=True, verbose_name='Interest Income')
    int_expense =                             models.CharField(max_length=25, null=True, blank=True, verbose_name='Interest Expense')
    net_int_income =                          models.CharField(max_length=25, null=True, blank=True, verbose_name='Net Interest Income')
    fees_comission_income =                   models.CharField(max_length=25, null=True, blank=True, verbose_name='Fees & Commission Income')
    fees_commission_exp =                     models.CharField(max_length=25, null=True, blank=True, verbose_name='Fees & Commission Expenses')
    net_fees_income =                         models.CharField(max_length=25, null=True, blank=True, verbose_name='Net fees & commission income')
    net_fees_interest_income =                models.CharField(max_length=25, null=True, blank=True, verbose_name='Net interest, fees & commission income')
    net_trading_income =                      models.CharField(max_length=25, null=True, blank=True, verbose_name='Net Trading Income')
    other_operating_income =                  models.CharField(max_length=25, null=True, blank=True, verbose_name='Other operating income')
    impairment_charge =                       models.CharField(max_length=25, null=True, blank=True, verbose_name='Impairment Charge')
    net_operating_income =                    models.CharField(max_length=25, null=True, blank=True, verbose_name='Net operating income')
    personnel_expenses =                      models.CharField(max_length=25, null=True, blank=True, verbose_name='Personnel Expenses')
    other_operating_exp =                     models.CharField(max_length=25, null=True, blank=True, verbose_name='Other operating expenses')
    depreciation =                            models.CharField(max_length=25, null=True, blank=True, verbose_name='Depreciation & Amortization')
    operating_profit =                        models.CharField(max_length=25, null=True, blank=True, verbose_name='Operating profit')
    non_operating_income =                    models.CharField(max_length=25, null=True, blank=True, verbose_name='Non operating income')
    non_operating_expense =                   models.CharField(max_length=25, null=True, blank=True, verbose_name='Non-operaing expenses')
    non_operating_pl_ratio =                  models.CharField(max_length=25, null=True, blank=True, verbose_name='Non-operating income/(expenses)')
    profit_bef_tax =                          models.CharField(max_length=25, null=True, blank=True, verbose_name='Profit before tax')
    income_tax =                              models.CharField(max_length=25, null=True, blank=True, verbose_name='Income tax')
    current_tax =                             models.CharField(max_length=25, null=True, blank=True, verbose_name='Current tax')
    deferred_tax =                            models.CharField(max_length=25, null=True, blank=True, verbose_name='Deferred tax')
    ratio_profit_loss =                       models.CharField(max_length=25, null=True, blank=True, verbose_name='Profit/Loss for the period')
    # int_income =                models.CharField(max_length=25, null=True, blank=True, verbose_name=)
    # int_income =                models.CharField(max_length=25, null=True, blank=True, verbose_name=)


    def __str__(self):
        return f'Income Statement of {self.company_name} for {self.year}'


class Liability(models.Model):
    company_name =              models.ForeignKey(Company, on_delete=models.CASCADE)
    year =                      models.CharField(max_length=20, verbose_name='Fiscal Year')

    borrowings =                models.CharField(max_length=25, null=True, blank=True, verbose_name='Borrowings')
    due_to_fbis =               models.CharField(max_length=25, null=True, blank=True, verbose_name='Due to B/FIs')
    due_to_nrb =                models.CharField(max_length=25, null=True, blank=True, verbose_name='Due to NRB')
    borrowing =                 models.CharField(max_length=25, null=True, blank=True, verbose_name='Borrowing')
    debt_securities =           models.CharField(max_length=25, null=True, blank=True, verbose_name='Debt Securities')
    deposits =                  models.CharField(max_length=25, null=True, blank=True, verbose_name='Deposits')
    other_liabilities =         models.CharField(max_length=25, null=True, blank=True, verbose_name='Other Liabilities')
    derive_fin_instruments =    models.CharField(max_length=25, null=True, blank=True, verbose_name='Derivative financial instruments')
    provisions =                models.CharField(max_length=25, null=True, blank=True, verbose_name='Provisions')
    current_tax_liab =          models.CharField(max_length=25, null=True, blank=True, verbose_name='Current tax liabilities')
    deferred_tax_liab =         models.CharField(max_length=25, null=True, blank=True, verbose_name='Deferred tax liabilities')
    subordinated_liab =         models.CharField(max_length=25, null=True, blank=True, verbose_name='Subordinated liabilities')
    other_liab =                models.CharField(max_length=25, null=True, blank=True, verbose_name='Other liabilities')
    total_liab =                models.CharField(max_length=25, null=True, blank=True, verbose_name='Total liabilities')
    
    # EQUITY section
    share_holder_equity =       models.CharField(max_length=25, null=True, blank=True, verbose_name='Share holders equity')
    paidup_capital =            models.CharField(max_length=25, null=True, blank=True, verbose_name='Paid up capital')
    reserves_surpluses =        models.CharField(max_length=25, null=True, blank=True, verbose_name='Reserves & Surpluses')
    shre_premium =              models.CharField(max_length=25, null=True, blank=True, verbose_name='Share Premium')
    retain_earnings =           models.CharField(max_length=25, null=True, blank=True, verbose_name='Retained Earnings')
    reserves =                  models.CharField(max_length=25, null=True, blank=True, verbose_name='Reserves')
    non_controll_interest =     models.CharField(max_length=25, null=True, blank=True, verbose_name='Non Controlling Interest')
    total_equity =              models.CharField(max_length=25, null=True, blank=True, verbose_name='Total Equity')
    total_liab_equity =         models.CharField(max_length=25, null=True, blank=True, verbose_name='Total liabilities & Equity')


    def __str__(self):
        return f'Liability and Equity of {self.company_name} for year {self.year}'