# Generated by Django 5.1.2 on 2024-11-07 13:15

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_trip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]