# Generated by Django 3.2.6 on 2021-10-18 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20210828_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, default='user_850dc16e-2ffc-11ec-8879-311be0840ff2', max_length=20, null=True, unique=True),
        ),
    ]