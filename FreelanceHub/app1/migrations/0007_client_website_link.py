# Generated by Django 5.0 on 2024-03-01 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_freelancer_freelancer_contarct'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='website_link',
            field=models.URLField(default=None),
        ),
    ]