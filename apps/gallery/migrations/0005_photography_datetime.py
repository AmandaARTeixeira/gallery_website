# Generated by Django 5.1.1 on 2024-09-17 03:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_photography_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='photography',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
