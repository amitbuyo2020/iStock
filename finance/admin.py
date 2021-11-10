from django.contrib import admin
from .models import Company, BalanceSheet, IncomeStatement, CashFlow



class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'category', 'listed_share', 'market_capital')
    list_filter = ()


    search_fields = ('name', )
    ordering = ('-market_capital', )


class BalanceSheetAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'year', 'total_assets')
    list_filter = ()

    fieldsets = (
        ('General', {
            'fields': ('company_name', 'year', 'cash_equiv', 'money_at_call', 'due_from_nrb', 'placement_with_bfis')
        }),
        ('Loans & Advances', {
            'fields': ('loans_advances', 'loans_advances_with_bfis', 'loans_to_customers')
        }),
        ('Investments', {
            'fields': ('investments', 'invest_security', 'invest_in_subsidiaries', 'invest_in_associtaes', 'property_investment')
        }),
        ('Assets', {
            'fields': ('other_assets', 'derive_fin_instruments', 'trading_assets', 'current_tax_assets', 'deferred_tax_assets',
                        'goodwill_assets', 'property_equipment'
            )
        }),
        ('Liabilities', {
            'fields': ('borrowings', 'due_to_fbis', 'due_to_nrb', 'borrowing', 'debt_securities', 
                        'deposits', 'other_liabilities', 'provisions',
                        'current_tax_liab', 'deferred_tax_liab', 'subordinated_liab', 'other_liab'
            )
        }),
        ('Equity', {
            'fields': ('share_holder_equity', 'paidup_capital', 'reserves_surpluses', 
                        'shre_premium', 'retain_earnings', 'reserves', 'non_controll_interest'
            )
        }),
        ('Total', {
            'fields': ('total_assets', 'total_liab', 'total_equity', 'total_liab_equity')
        })
    )

    search_fields = ('year', )
    ordering = ('company_name', '-year')




class IncomeStatementAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'year', )
    list_filter = ()

    fieldsets = (
        ('General', {
            'fields': ('company_name', 'year')
        }),
        ('Income', {
            'fields': ('int_income', 'net_int_income', 'fees_comission_income', 'net_fees_income', 'net_fees_interest_income', 
                        'net_trading_income', 'other_operating_income', 'net_operating_income', 'operating_profit', 'non_operating_income'
            )
        }),
        ('Expenses', {
            'fields': ('int_expense', 'fees_commission_exp', 'impairment_charge', 'personnel_expenses', 'other_operating_exp'
                        , 'depreciation', 'non_operating_expense'
            )
        }),
        ('Tax', {
            'fields': ('non_operating_pl_ratio', 'ratio_profit_loss', 'profit_bef_tax', 'income_tax', 'current_tax', 'deferred_tax')
        }) 
    )

    ordering = ('company_name', )


class CashFlowAdmin(admin.ModelAdmin):
    list_display = ('company', 'year', )

    fieldsets = (
        ('General', {
            'fields': ('company', 'year')
        }),
        ('Cash Flow from Operating Activities', {
            'fields': (
                        'fee_other_income', 'dividend', 'interest_received',
                        'receipt_from_other', 'other_income',
                        'interest_paid', 'commission_fees_paid', 'office_operating_expenses',
                        'cash_pay_to_employee', 'other_expense_paid', 'operating_cashflow_before',
                        'ratio_inc_dec_op_assets', 'due_from_nrb', 'placement_with_banks',
                        'other_trading_assets', 'loans_advances', 'loans_advances_to_banks',
                        'loans_advances_to_customers', 'other_assets', 'ratio_operating_liab',
                        'due_to_bank', 'due_to_nrb', 'deposit_from_customers', 'borrowings',
                        'other_liabs', 'net_cashflow_before_tax', 'income_tax_paid', 
                        'net_cashflow_operating_activities'
                    )
        }),
        ('Cash Flow from Investing Activities', {
            'fields': (
                'netInvestment_in_investings', 'purchase_investment_securities', 'reciepts_investment_securities',
                'netInvestment_property_equipment', 'purchase_property_equipment', 'reciept_property_equipment',
                'purchase_intangible_assets', 'reciept_intangible_assets', 'purchase_invest_properties',
                'reciept_invest_properties', 'recieved_interest', 'recieved_dividend', 'investment_in_associates',
                'others', 'net_cash_in_investment'
            )
        }),
        ('Cash Flow from Financing Activities', {
            'fields': (
                'repayment_debt_securities', 'reciept_subordinate_liabs', 'repayment_subordinate_liabs',
                'reciept_share_issue', 'paid_dividends', 'paid_interest', 'ratio_facilties_from_nrb',
                'other_reciept_payment', 'net_cash_financing', 'net_ratio_cashEquivalence', 'cashEquivalence_at_fiscal_year',
                'effect_exchangeRate_fluctuations'
            )
        }),
        ('Cash and Cash Equivalence at the end of fiscal year', {
            'fields': ('cashEquivalence_endOf_fiscalYear', )
        })
    )
    ordering = ('company', '-year')




admin.site.site_header = 'iStock'
admin.site.register(IncomeStatement, IncomeStatementAdmin)
admin.site.register(BalanceSheet, BalanceSheetAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(CashFlow, CashFlowAdmin)
