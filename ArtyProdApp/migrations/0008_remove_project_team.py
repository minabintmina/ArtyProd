# Generated by Django 4.2 on 2023-05-16 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ArtyProdApp', '0007_remove_personnel_service_remove_project_service_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='team',
        ),
    ]
