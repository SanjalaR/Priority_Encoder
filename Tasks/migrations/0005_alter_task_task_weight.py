# Generated by Django 5.1.4 on 2024-12-08 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0004_task_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_weight',
            field=models.FloatField(),
        ),
    ]
