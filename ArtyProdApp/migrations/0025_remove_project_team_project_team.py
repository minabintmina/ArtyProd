# Generated by Django 4.2 on 2023-05-17 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtyProdApp', '0024_alter_project_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='team',
        ),
        migrations.AddField(
            model_name='project',
            name='team',
            field=models.ManyToManyField(to='ArtyProdApp.team'),
        ),
    ]
