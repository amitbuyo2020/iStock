from django.contrib import admin

from .models import Category, Company, Asset, Liability, IncomeStatement



class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'established_date', 'category')
    list_filter = ()


    search_fields = ('name', )
    ordering = ('name', )


class AssetAdmin(admin.ModelAdmin):
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
        ('Total', {
            'fields': ('total_assets', )
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

class LiabilityAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'year', 'total_liab_equity')
    list_filter = ()

    fieldsets = (
        ('General', {
            'fields': ('company_name', 'year')
        }),
        ('Liabilities', {
            'fields': ('borrowings', 'due_to_fbis', 'due_to_nrb', 'borrowing', 'debt_securities', 
                        'deposits', 'other_liabilities', 'derive_fin_instruments', 'provisions',
                        'current_tax_liab', 'deferred_tax_liab', 'subordinated_liab', 'other_liab'
            )
        }),
        ('Equity', {
            'fields': ('share_holder_equity', 'paidup_capital', 'reserves_surpluses', 
                        'shre_premium', 'retain_earnings', 'reserves', 'non_controll_interest'
            )
        }),
        ('Total Liabilities & Equity', {
            'fields': ('total_liab', 'total_equity', 'total_liab_equity')
        })
    )
    ordering = ('company_name', )


admin.site.register(Category)
admin.site.register(Liability, LiabilityAdmin)
admin.site.register(IncomeStatement, IncomeStatementAdmin)
admin.site.register(Asset, AssetAdmin)
admin.site.register(Company, CompanyAdmin)
