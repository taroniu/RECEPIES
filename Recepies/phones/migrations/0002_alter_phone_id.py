# Generated by Django 4.2.9 on 2024-02-25 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]