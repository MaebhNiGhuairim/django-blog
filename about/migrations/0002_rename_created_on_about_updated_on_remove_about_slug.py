# Generated by Django 4.2.17 on 2025-01-13 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='created_on',
            new_name='updated_on',
        ),
        migrations.RemoveField(
            model_name='about',
            name='slug',
        ),
    ]
