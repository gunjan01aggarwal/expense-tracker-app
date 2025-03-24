# Generated by Django 3.2.25 on 2025-02-12 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money_manager', '0002_auto_20250207_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('Hospital', 'Hospital'), ('Entertainment', 'Entertainment'), ('Shopping', 'Shopping'), ('Necessities', 'Necessities'), ('Others', 'Others'), ('Select Category', 'Select Category'), ('Food', 'Food'), ('Education', 'Education'), ('Travel', 'Travel')], default='Select Category', max_length=100),
        ),
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
