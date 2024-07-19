# Generated by Django 5.0.6 on 2024-05-27 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('dob', models.IntegerField(default=None, max_length=9)),
                ('email', models.EmailField(default=None, max_length=200)),
                ('phone', models.IntegerField(default=None, max_length=11)),
                ('gender', models.CharField(default=None, max_length=10)),
                ('branch', models.CharField(default=None, max_length=50)),
                ('passing_year', models.IntegerField(default=None, max_length=5)),
                ('percentage', models.IntegerField(default=None, max_length=3)),
                ('school', models.CharField(default=None, max_length=200)),
                ('school_district', models.CharField(default=None, max_length=50)),
                ('admit_card', models.ImageField(default=None, null=True, upload_to='admitcard/')),
                ('marksheet', models.ImageField(default=None, null=True, upload_to='marksheet/')),
                ('street', models.CharField(default=None, max_length=20)),
                ('village', models.CharField(default=None, max_length=60)),
                ('state', models.CharField(default=None, max_length=20)),
                ('district', models.CharField(default=None, max_length=20)),
                ('block', models.PositiveIntegerField(default=None)),
                ('pin', models.IntegerField(default=None, max_length=7)),
            ],
            options={
                'db_table': 'Student_table',
            },
        ),
    ]
