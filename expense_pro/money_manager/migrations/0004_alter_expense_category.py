# Generated by Django 3.2.25 on 2025-02-21 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money_manager', '0003_auto_20250212_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('Entertainment', 'Entertainment'), ('Necessities', 'Necessities'), ('Food', 'Food'), ('Others', 'Others'), ('Travel', 'Travel'), ('Shopping', 'Shopping'), ('Education', 'Education'), ('Hospital', 'Hospital')], default=None, max_length=100),
        ),
    ]
