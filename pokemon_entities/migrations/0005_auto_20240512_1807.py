# Generated by Django 3.1.14 on 2024-05-12 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_auto_20240510_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(blank=True, upload_to='images', verbose_name='Image'),
        ),
    ]
