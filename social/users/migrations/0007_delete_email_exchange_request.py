# Generated by Django 5.1.1 on 2024-11-18 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_email_exchange_request'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Email_exchange_request',
        ),
    ]