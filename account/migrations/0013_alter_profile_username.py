# Generated by Django 3.2.6 on 2021-10-20 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_alter_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, default='user_2b470af0-3173-11ec-967e-c76b8ca1be3d', max_length=20, null=True, unique=True),
        ),
    ]
