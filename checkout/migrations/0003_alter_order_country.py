# Generated by Django 5.1.2 on 2024-11-07 09:19

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_order_stripe_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
