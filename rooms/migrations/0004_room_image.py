# Generated by Django 5.1.2 on 2024-10-29 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_room_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
