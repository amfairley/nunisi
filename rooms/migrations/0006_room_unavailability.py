# Generated by Django 5.1.2 on 2024-10-29 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_room_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='unavailability',
            field=models.JSONField(blank=True, default=list),
        ),
    ]
