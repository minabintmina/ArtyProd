# Generated by Django 4.2 on 2023-05-06 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ArtyProdApp', '0002_personnel_services_alter_contact_phonenumber_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(default='', max_length=50)),
                ('description', models.TextField(default='', max_length=500)),
                ('start_date', models.DateField(default='')),
                ('end_date', models.DateField()),
                ('status', models.CharField(choices=[('C', 'Completed'), ('I', 'In-progress')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('username', models.CharField(default='', max_length=100, unique=True)),
                ('email', models.EmailField(default='', max_length=100, unique=True)),
                ('password', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='password',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phonenumber',
        ),
        migrations.RemoveField(
            model_name='team',
            name='Teams',
        ),
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='contact',
            name='text',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='team',
            name='personnel',
            field=models.ManyToManyField(to='ArtyProdApp.personnel'),
        ),
        migrations.AlterField(
            model_name='services',
            name='TypeS',
            field=models.CharField(choices=[('G', 'Graphical charter'), ('O', 'Object 3D'), ('S', 'Scenarisation')], max_length=1),
        ),
        migrations.AddField(
            model_name='team',
            name='project',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ArtyProdApp.project'),
            preserve_default=False,
        ),
    ]
