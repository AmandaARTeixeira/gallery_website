# Generated by Django 5.1.1 on 2024-09-17 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_photography_caption_photography_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='photography',
            name='category',
            field=models.CharField(choices=[('NEBULOSA', 'Nebulosa'), ('ESTRELA', 'Estrela'), ('GALÁXIA', 'Galáxia'), ('PLANETA', 'Planeta')], default='', max_length=100),
        ),
    ]
