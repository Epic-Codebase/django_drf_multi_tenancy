# Generated by Django 4.0 on 2025-02-25 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='hotel_pictures/'),
        ),
    ]
