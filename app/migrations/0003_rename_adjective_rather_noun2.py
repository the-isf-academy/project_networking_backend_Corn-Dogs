# Generated by Django 5.1.2 on 2024-10-15 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rather_happy_rather_timechosen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rather',
            old_name='adjective',
            new_name='noun2',
        ),
    ]
