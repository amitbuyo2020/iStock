# Generated by Django 3.2.6 on 2021-10-19 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, default='user_0feb5174-3099-11ec-b597-c330b1f947ef', max_length=20, null=True, unique=True),
        ),
    ]
