# Generated by Django 4.2 on 2023-05-16 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtyProdApp', '0016_alter_personnel_services_alter_project_services_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='services',
            field=models.ManyToManyField(to='ArtyProdApp.services'),
        ),
    ]
