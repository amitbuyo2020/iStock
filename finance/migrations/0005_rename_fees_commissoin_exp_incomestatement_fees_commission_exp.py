# Generated by Django 3.2.6 on 2021-10-19 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_incomestatement_liability'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incomestatement',
            old_name='fees_commissoin_exp',
            new_name='fees_commission_exp',
        ),
    ]