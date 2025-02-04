# Generated by Django 5.0 on 2024-03-30 16:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app1', '0009_remove_client_user_remove_freelancer_user'),
        ('project_management', '0003_delete_project_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='project_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('Project_discription', models.CharField(max_length=10000)),
                ('discription_image', models.ImageField(default=None, upload_to='project_dis_image')),
                ('discription_video', models.FileField(default=None, upload_to='dis_video')),
                ('amount', models.CharField(max_length=50)),
                ('client_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.client')),
            ],
        ),
    ]
