# Generated by Django 3.1.14 on 2024-05-08 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='image',
            field=models.FileField(blank=True, upload_to='images', verbose_name='Image'),
        ),
    ]