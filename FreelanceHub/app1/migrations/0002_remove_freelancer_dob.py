# Generated by Django 5.0 on 2024-02-28 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='freelancer',
            name='DOB',
        ),
    ]
