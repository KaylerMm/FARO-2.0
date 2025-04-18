# Generated by Django 5.2 on 2025-04-13 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('phone_2', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
