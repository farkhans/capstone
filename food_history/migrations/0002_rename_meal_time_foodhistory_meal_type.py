# Generated by Django 5.0.1 on 2024-06-08 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_history', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodhistory',
            old_name='meal_time',
            new_name='meal_type',
        ),
    ]