# Generated by Django 5.1.1 on 2024-09-17 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_photography_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='photography',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
