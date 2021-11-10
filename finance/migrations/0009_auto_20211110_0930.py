# Generated by Django 3.2.6 on 2021-11-10 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0008_auto_20211102_0935'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Companies'},
        ),
        migrations.CreateModel(
            name='CashFlow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=20, verbose_name='Fiscal Year')),
                ('cashflow_operating_activities', models.CharField(blank=True, max_length=25, null=True, verbose_name='Cash Flow from operating activities')),
                ('interest_received', models.CharField(blank=True, max_length=25, null=True, verbose_name='Interest Received')),
                ('fee_other_income', models.CharField(blank=True, max_length=25, null=True, verbose_name='Fees and other income received')),
                ('dividend', models.CharField(blank=True, max_length=25, null=True, verbose_name='Dividend received')),
                ('receipt_from_other', models.CharField(blank=True, max_length=25, null=True, verbose_name='Receipts from other operating activities')),
                ('other_income', models.CharField(blank=True, max_length=25, null=True, verbose_name='Other Income')),
                ('interest_paid', models.CharField(blank=True, max_length=25, null=True, verbose_name='Interest paid')),
                ('commission_fees_paid', models.CharField(blank=True, max_length=25, null=True, verbose_name='Commission and fees paid')),
                ('office_operating_expenses', models.CharField(blank=True, max_length=25, null=True, verbose_name='Office Operating Expenses')),
                ('cash_pay_to_employee', models.CharField(blank=True, max_length=25, null=True, verbose_name='Cash payment to employees')),
                ('other_expense_paid', models.CharField(blank=True, max_length=25, null=True, verbose_name='Other expense paid')),
                ('operating_cashflow_before', models.CharField(blank=True, max_length=25, null=True, verbose_name='Operating cash flows before changes in operating assets and liabilities')),
                ('ratio_inc_dec_op_assets', models.CharField(blank=True, max_length=25, null=True, verbose_name='(Increase)/(Decrease) in operating assets')),
                ('due_from_nrb', models.CharField(blank=True, max_length=25, null=True, verbose_name='Due from Nepal Rastra Bank')),
                ('placement_with_banks', models.CharField(blank=True, max_length=25, null=True, verbose_name='Placement with bank and financial institutions')),
                ('other_trading_assets', models.CharField(blank=True, max_length=25, null=True, verbose_name='Other trading assets')),
                ('loans_advances', models.CharField(blank=True, max_length=25, null=True, verbose_name='Loan and Advances')),
                ('loans_advances_to_banks', models.CharField(blank=True, max_length=25, null=True, verbose_name='Loan and advances to bank and financial institutions')),
                ('loans_advances_to_customers', models.CharField(blank=True, max_length=25, null=True, verbose_name='Loan and advances to customers')),
                ('other_assets', models.CharField(blank=True, max_length=25, null=True, verbose_name='Other assets')),
                ('ratio_operating_liab', models.CharField(blank=True, max_length=25, null=True, verbose_name='Increase/ (Decrease) in operating liabilites')),
                ('due_to_bank', models.CharField(blank=True, max_length=25, null=True, verbose_name='Due to bank and financial institutions')),
                ('due_to_nrb', models.CharField(blank=True, max_length=25, null=True, verbose_name='Due to Nepal Rastra Bank')),
                ('deposit_from_customers', models.CharField(blank=True, max_length=25, null=True, verbose_name='Deposit from customers')),
                ('borrowings', models.CharField(blank=True, max_length=25, null=True, verbose_name='Borrowings')),
                ('other_liabs', models.CharField(blank=True, max_length=25, null=True, verbose_name='Other Liabilities')),
                ('net_cashflow_before_tax', models.CharField(blank=True, max_length=25, null=True, verbose_name='Net cash flow from operating activities before tax paid')),
                ('income_tax_paid', models.CharField(blank=True, max_length=25, null=True, verbose_name='Income taxes paid')),
                ('net_cashflow_operating_activities', models.CharField(blank=True, max_length=25, null=True, verbose_name='Net cash flow from operating activities')),
                ('cashflow_investing', models.CharField(blank=True, max_length=25, null=True, verbose_name='Cash Flow from Investing Activities')),
                ('netInvestment_in_investings', models.CharField(blank=True, max_length=25, null=True, verbose_name='Net investment in investment properties')),
                ('purchase_investment_securities', models.CharField(blank=True, max_length=25, null=True, verbose_name='Purchase of investment securities')),
                ('reciepts_investment_securities', models.CharField(blank=True, max_length=25, null=True, verbose_name='Receipts from sale of investment securities')),
                ('netInvestment_property_equipment', models.CharField(blank=True, max_length=25, null=True, verbose_name='Net investment in property and equipment')),
                ('purchase_property_equipment', models.CharField(blank=True, max_length=25, null=True, verbose_name='Purchase of property and equipment')),
                ('reciept_property_equipment', models.CharField(blank=True, max_length=25, null=True, verbose_name='Receipt from the sale of property and equipment')),
                ('purchase_intangible_assets', models.CharField(blank=True, max_length=25, null=True, verbose_name='Purchase of intangible assets')),
                ('reciept_intangible_assets', models.CharField(blank=True, max_length=25, null=True, verbose_name='Receipt from the sale of intangible assets')),
                ('purchase_invest_properties', models.CharField(blank=True, max_length=25, null=True, verbose_name='Purchase of investment properties')),
                ('reciept_invest_properties', models.CharField(blank=True, max_length=25, null=True, verbose_name='Receipt from the sale of investment properties')),
                ('recieved_interest', models.CharField(blank=True, max_length=25, null=True, verbose_name='Interest received')),
                ('recieved_dividend', models.CharField(blank=True, max_length=25, null=True, verbose_name='Dividend received')),
                ('investment_in_associates', models.CharField(blank=True, max_length=25, null=True, verbose_name='Investment in associates, subisdary and other company')),
                ('others', models.CharField(blank=True, max_length=25, null=True, verbose_name='Others')),
                ('net_cash_in_investment', models.CharField(blank=True, max_length=25, null=True, verbose_name='Net cash used in investing activities (B)')),
                ('cashflow_financing', models.CharField(blank=True, max_length=25, null=True, verbose_name='Cash Flow from Financing Activites')),
                ('repayment_debt_securities', models.CharField(blank=True, max_length=25, null=True, verbose_name='Repayment of debt securities')),
                ('reciept_subordinate_liabs', models.CharField(blank=True, max_length=25, null=True, verbose_name='Receipt from issue of subordinated liabilities')),
                ('repayment_subordinate_liabs', models.CharField(blank=True, max_length=25, null=True, verbose_name='Repayment of subordinated liabilities')),
                ('reciept_share_issue', models.CharField(blank=True, max_length=25, null=True, verbose_name='Receipt from issue of shares')),
                ('paid_dividends', models.CharField(blank=True, max_length=25, null=True, verbose_name='Dividends paid')),
                ('paid_interest', models.CharField(blank=True, max_length=25, null=True, verbose_name='Interest paid')),
                ('ratio_facilties_from_nrb', models.CharField(blank=True, max_length=25, null=True, verbose_name='Increase/Decrease in Refinance/facilities received from NRB')),
                ('other_reciept_payment', models.CharField(blank=True, max_length=25, null=True, verbose_name='Other receipt/payment')),
                ('net_cash_financing', models.CharField(blank=True, max_length=25, null=True, verbose_name='Net cash from financing activities')),
                ('net_ratio_cashEquivalence', models.CharField(blank=True, max_length=25, null=True, verbose_name='Net increase (decrease) in cash and cash equivalents')),
                ('cashEquivalence_at_fiscal_year', models.CharField(blank=True, max_length=25, null=True, verbose_name='Cash and cash equivalents at Shrawan 01 (beginning of the year)')),
                ('effect_exchangeRate_fluctuations', models.CharField(blank=True, max_length=25, null=True, verbose_name='Effect of exchange rate fluctuations on cash and cash equivalents held')),
                ('cashEquivalence_endOf_fiscalYear', models.CharField(blank=True, max_length=25, null=True, verbose_name='Cash and cash equivalents at Asar end (end of the year)')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.company')),
            ],
        ),
    ]
