# Generated by Django 5.1.5 on 2025-01-17 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('userEmail', models.EmailField(max_length=254)),
                ('dataDeNascimento', models.DateField()),
                ('senhaUser', models.CharField(max_length=500)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
