# Generated by Django 5.0 on 2024-03-30 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0002_remove_project_post_payment_method'),
    ]

    operations = [
        migrations.DeleteModel(
            name='project_post',
        ),
    ]
