# Generated by Django 5.0 on 2024-03-08 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_client_user_freelancer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
        migrations.RemoveField(
            model_name='freelancer',
            name='user',
        ),
    ]
