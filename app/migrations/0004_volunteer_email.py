# Generated by Django 5.1 on 2024-09-20 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_doantiondate_donation_donationdate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='email',
            field=models.EmailField(blank=True, max_length=60, null=True),
        ),
    ]
