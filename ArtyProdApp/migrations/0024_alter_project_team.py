# Generated by Django 4.2 on 2023-05-17 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ArtyProdApp', '0023_remove_team_project_project_team_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ArtyProdApp.team'),
        ),
    ]
