# Generated by Django 5.1.2 on 2024-12-12 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0010_alter_amenities_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]