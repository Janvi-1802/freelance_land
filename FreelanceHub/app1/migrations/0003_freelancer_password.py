# Generated by Django 5.0 on 2024-02-28 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_remove_freelancer_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='freelancer',
            name='password',
            field=models.TextField(default=0),
        ),
    ]
