from django.db import models


CHOICES = [
    ('Development Bank', 'Development Bank'),
    ('Commercial Bank', 'Commercial Bank'),
    ('Microfinance', 'Microfinance'),
    ('Hydropower', 'Hydropower'),
    ('Hotels', 'Hotels'),
    ('Life Insurance', 'Life Insurance')
]

class Company(models.Model):
    name = models.CharField(max_length=200, verbose_name='Company Name', unique=True)
    established_date = models.DateField(blank=True, null=True)
    category = models.CharField(max_length=100, choices=CHOICES)
    symbol = models.CharField(max_length=15, null=True, blank=True, unique=True)
    listed_share = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    market_capital = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)

    
    class Meta:
        verbose_name_plural = 'Companies'


    def __str__(self):
        return self.name


class BalanceSheet(models.Model):
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
   


    def __str__(self):
        return self.net_int_income


class CashFlow(models.Model):
    company                                 = models.ForeignKey(Company, on_delete=models.CASCADE)
    year                                    = models.CharField(max_length=20, verbose_name='Fiscal Year')


    #  cashflow_operating_activities           
    interest_received                       = models.CharField(max_length=25, null=True, blank=True, verbose_name="Interest Received")
    fee_other_income                        = models.CharField(max_length=25, null=True, blank=True, verbose_name="Fees and other income received")
    dividend                                = models.CharField(max_length=25, null=True, blank=True, verbose_name="Dividend received")
    receipt_from_other                      = models.CharField(max_length=25, null=True, blank=True, verbose_name="Receipts from other operating activities")
    other_income                            = models.CharField(max_length=25, null=True, blank=True, verbose_name="Other Income")
    interest_paid                           = models.CharField(max_length=25, null=True, blank=True, verbose_name="Interest paid")
    commission_fees_paid                    = models.CharField(max_length=25, null=True, blank=True, verbose_name="Commission and fees paid")
    office_operating_expenses               = models.CharField(max_length=25, null=True, blank=True, verbose_name="Office Operating Expenses")
    cash_pay_to_employee                    = models.CharField(max_length=25, null=True, blank=True, verbose_name="Cash payment to employees")
    other_expense_paid                      = models.CharField(max_length=25, null=True, blank=True, verbose_name="Other expense paid")
    operating_cashflow_before               = models.CharField(max_length=25, null=True, blank=True, verbose_name="Operating cash flows before changes in operating assets and liabilities")
    ratio_inc_dec_op_assets                 = models.CharField(max_length=25, null=True, blank=True, verbose_name="(Increase)/(Decrease) in operating assets")
    due_from_nrb                            = models.CharField(max_length=25, null=True, blank=True, verbose_name="Due from Nepal Rastra Bank")
    placement_with_banks                    = models.CharField(max_length=25, null=True, blank=True, verbose_name="Placement with bank and financial institutions")
    other_trading_assets                    = models.CharField(max_length=25, null=True, blank=True, verbose_name="Other trading assets")
    loans_advances                          = models.CharField(max_length=25, null=True, blank=True, verbose_name="Loan and Advances")
    loans_advances_to_banks                 = models.CharField(max_length=25, null=True, blank=True, verbose_name="Loan and advances to bank and financial institutions")
    loans_advances_to_customers             = models.CharField(max_length=25, null=True, blank=True, verbose_name="Loan and advances to customers")
    other_assets                            = models.CharField(max_length=25, null=True, blank=True, verbose_name="Other assets")
    ratio_operating_liab                    = models.CharField(max_length=25, null=True, blank=True, verbose_name="Increase/ (Decrease) in operating liabilites")
    due_to_bank                             = models.CharField(max_length=25, null=True, blank=True, verbose_name="Due to bank and financial institutions")
    due_to_nrb                              = models.CharField(max_length=25, null=True, blank=True, verbose_name="Due to Nepal Rastra Bank")
    deposit_from_customers                  = models.CharField(max_length=25, null=True, blank=True, verbose_name="Deposit from customers")
    borrowings                              = models.CharField(max_length=25, null=True, blank=True, verbose_name="Borrowings")
    other_liabs                             = models.CharField(max_length=25, null=True, blank=True, verbose_name="Other Liabilities")
    net_cashflow_before_tax                 = models.CharField(max_length=25, null=True, blank=True, verbose_name="Net cash flow from operating activities before tax paid")
    income_tax_paid                         = models.CharField(max_length=25, null=True, blank=True, verbose_name="Income taxes paid")
    net_cashflow_operating_activities       = models.CharField(max_length=25, null=True, blank=True, verbose_name="Net cash flow from operating activities")
    
    
    #  Cashflow from investment activities                 
    netInvestment_in_investings             = models.CharField(max_length=25, null=True, blank=True, verbose_name="Net investment in investment properties")
    purchase_investment_securities          = models.CharField(max_length=25, null=True, blank=True, verbose_name="Purchase of investment securities")
    reciepts_investment_securities          = models.CharField(max_length=25, null=True, blank=True, verbose_name="Receipts from sale of investment securities")
    netInvestment_property_equipment        = models.CharField(max_length=25, null=True, blank=True, verbose_name="Net investment in property and equipment")
    purchase_property_equipment             = models.CharField(max_length=25, null=True, blank=True, verbose_name="Purchase of property and equipment")
    reciept_property_equipment              = models.CharField(max_length=25, null=True, blank=True, verbose_name="Receipt from the sale of property and equipment")
    purchase_intangible_assets              = models.CharField(max_length=25, null=True, blank=True, verbose_name="Purchase of intangible assets")
    reciept_intangible_assets               = models.CharField(max_length=25, null=True, blank=True, verbose_name="Receipt from the sale of intangible assets")
    purchase_invest_properties              = models.CharField(max_length=25, null=True, blank=True, verbose_name="Purchase of investment properties")
    reciept_invest_properties               = models.CharField(max_length=25, null=True, blank=True, verbose_name="Receipt from the sale of investment properties")
    recieved_interest                       = models.CharField(max_length=25, null=True, blank=True, verbose_name="Interest received")
    recieved_dividend                       = models.CharField(max_length=25, null=True, blank=True, verbose_name="Dividend received")
    investment_in_associates                = models.CharField(max_length=25, null=True, blank=True, verbose_name="Investment in associates, subisdary and other company")
    others                                  = models.CharField(max_length=25, null=True, blank=True, verbose_name="Others")
    net_cash_in_investment                  = models.CharField(max_length=25, null=True, blank=True, verbose_name="Net cash used in investing activities (B)")
    
    # cashflow from financing activities
    repayment_debt_securities               = models.CharField(max_length=25, null=True, blank=True, verbose_name="Repayment of debt securities")
    reciept_subordinate_liabs               = models.CharField(max_length=25, null=True, blank=True, verbose_name="Receipt from issue of subordinated liabilities")
    repayment_subordinate_liabs             = models.CharField(max_length=25, null=True, blank=True, verbose_name="Repayment of subordinated liabilities")
    reciept_share_issue                     = models.CharField(max_length=25, null=True, blank=True, verbose_name="Receipt from issue of shares")
    paid_dividends                          = models.CharField(max_length=25, null=True, blank=True, verbose_name="Dividends paid")
    paid_interest                           = models.CharField(max_length=25, null=True, blank=True, verbose_name="Interest paid")
    ratio_facilties_from_nrb                = models.CharField(max_length=25, null=True, blank=True, verbose_name="Increase/Decrease in Refinance/facilities received from NRB")
    other_reciept_payment                   = models.CharField(max_length=25, null=True, blank=True, verbose_name="Other receipt/payment")
    net_cash_financing                      = models.CharField(max_length=25, null=True, blank=True, verbose_name="Net cash from financing activities")
    net_ratio_cashEquivalence               = models.CharField(max_length=25, null=True, blank=True, verbose_name="Net increase (decrease) in cash and cash equivalents")
    cashEquivalence_at_fiscal_year          = models.CharField(max_length=25, null=True, blank=True, verbose_name="Cash and cash equivalents at Shrawan 01 (beginning of the year)")
    effect_exchangeRate_fluctuations        = models.CharField(max_length=25, null=True, blank=True, verbose_name="Effect of exchange rate fluctuations on cash and cash equivalents held")
    cashEquivalence_endOf_fiscalYear        = models.CharField(max_length=25, null=True, blank=True, verbose_name="Cash and cash equivalents at Asar end (end of the year)")
