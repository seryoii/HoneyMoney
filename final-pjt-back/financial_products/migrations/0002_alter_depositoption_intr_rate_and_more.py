# Generated by Django 4.2.8 on 2024-05-21 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depositoption',
            name='intr_rate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='depositoption',
            name='intr_rate2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='savingoption',
            name='intr_rate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='savingoption',
            name='intr_rate2',
            field=models.FloatField(null=True),
        ),
    ]