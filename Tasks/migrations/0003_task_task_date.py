# Generated by Django 5.1.4 on 2024-12-05 13:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0002_rename_tasklist_account_tasklist'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_date',
            field=models.DateField(default=datetime.datetime(2024, 12, 5, 19, 25, 43, 245602)),
            preserve_default=False,
        ),
    ]
