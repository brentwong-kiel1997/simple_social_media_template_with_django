# Generated by Django 5.1.1 on 2024-11-26 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post_comment',
            options={'ordering': ['-created']},
        ),
    ]