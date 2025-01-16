# Generated by Django 5.1.5 on 2025-01-16 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReceitasDespesas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.IntegerField(default=2)),
                ('valor', models.FloatField(default=0.0)),
                ('dataDaMovimentacao', models.DateTimeField()),
                ('descrição', models.CharField(max_length=500)),
                ('usuario_id', models.IntegerField()),
            ],
        ),
    ]
