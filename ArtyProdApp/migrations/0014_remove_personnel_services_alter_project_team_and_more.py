# Generated by Django 4.2 on 2023-05-16 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ArtyProdApp', '0013_alter_project_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personnel',
            name='services',
        ),
        migrations.AlterField(
            model_name='project',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArtyProdApp.team'),
        ),
        migrations.AddField(
            model_name='personnel',
            name='services',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ArtyProdApp.services'),
            preserve_default=False,
        ),
    ]