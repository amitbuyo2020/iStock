# Generated by Django 3.2.6 on 2021-11-10 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_alter_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, default='user_b3c32290-41d8-11ec-b92e-b74cdd34232a', max_length=20, null=True, unique=True),
        ),
    ]